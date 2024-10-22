# Results vs. base

- fork: faster-cpython
- ref: experimental_gc_fix
- machine: linux-x86_64
- commit hash: 9d28e99
- commit date: 2024-09-27
- overall geometric mean: 1.04x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.95x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240926-linux-x86_64-python-2c472d36b776636fb008-3.14.0a0-2c472d3 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-9d28e99 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 256 ms                                                                | 272 ms: 1.06x slower                                                           |
| docutils       | 2.65 sec                                                              | 2.77 sec: 1.05x slower                                                         |
| html5lib       | 63.7 ms                                                               | 68.1 ms: 1.07x slower                                                          |
| tornado_http   | 90.1 ms                                                               | 91.5 ms: 1.02x slower                                                          |
| Geometric mean | (ref)                                                                 | 1.05x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240926-linux-x86_64-python-2c472d36b776636fb008-3.14.0a0-2c472d3 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-9d28e99 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 1.79 sec                                                              | 1.78 sec: 1.00x faster                                                         |
| asyncio_tcp                | 472 ms                                                                | 480 ms: 1.02x slower                                                           |
| coroutines                 | 22.6 ms                                                               | 23.6 ms: 1.05x slower                                                          |
| async_generators           | 438 ms                                                                | 459 ms: 1.05x slower                                                           |
| async_tree_io_tg           | 874 ms                                                                | 966 ms: 1.10x slower                                                           |
| async_tree_cpu_io_mixed    | 573 ms                                                                | 638 ms: 1.11x slower                                                           |
| async_tree_io              | 883 ms                                                                | 995 ms: 1.13x slower                                                           |
| async_tree_cpu_io_mixed_tg | 559 ms                                                                | 635 ms: 1.13x slower                                                           |
| async_tree_memoization     | 396 ms                                                                | 489 ms: 1.24x slower                                                           |
| async_tree_memoization_tg  | 390 ms                                                                | 498 ms: 1.28x slower                                                           |
| async_tree_none_tg         | 303 ms                                                                | 390 ms: 1.29x slower                                                           |
| async_tree_none            | 317 ms                                                                | 424 ms: 1.34x slower                                                           |
| Geometric mean             | (ref)                                                                 | 1.13x slower                                                                   |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240926-linux-x86_64-python-2c472d36b776636fb008-3.14.0a0-2c472d3 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-9d28e99 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 187 ms                                                                | 187 ms: 1.00x slower                                                           |
| float          | 77.1 ms                                                               | 97.0 ms: 1.26x slower                                                          |
| Geometric mean | (ref)                                                                 | 1.08x slower                                                                   |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240926-linux-x86_64-python-2c472d36b776636fb008-3.14.0a0-2c472d3 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-9d28e99 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 237 ms                                                                | 223 ms: 1.07x faster                                                           |
| regex_effbot   | 3.87 ms                                                               | 3.67 ms: 1.06x faster                                                          |
| regex_compile  | 128 ms                                                                | 128 ms: 1.00x slower                                                           |
| regex_v8       | 24.3 ms                                                               | 24.5 ms: 1.01x slower                                                          |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240926-linux-x86_64-python-2c472d36b776636fb008-3.14.0a0-2c472d3 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-9d28e99 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| unpickle             | 14.7 us                                                               | 14.5 us: 1.01x faster                                                          |
| unpickle_pure_python | 216 us                                                                | 215 us: 1.00x faster                                                           |
| pickle_pure_python   | 303 us                                                                | 305 us: 1.00x slower                                                           |
| json_loads           | 26.9 us                                                               | 27.1 us: 1.01x slower                                                          |
| pickle_dict          | 34.6 us                                                               | 34.8 us: 1.01x slower                                                          |
| pickle               | 11.6 us                                                               | 11.7 us: 1.01x slower                                                          |
| unpickle_list        | 5.16 us                                                               | 5.22 us: 1.01x slower                                                          |
| json_dumps           | 10.3 ms                                                               | 10.4 ms: 1.01x slower                                                          |
| pickle_list          | 5.14 us                                                               | 5.36 us: 1.04x slower                                                          |
| xml_etree_generate   | 85.3 ms                                                               | 93.0 ms: 1.09x slower                                                          |
| xml_etree_process    | 58.7 ms                                                               | 65.1 ms: 1.11x slower                                                          |
| xml_etree_parse      | 155 ms                                                                | 184 ms: 1.19x slower                                                           |
| xml_etree_iterparse  | 104 ms                                                                | 150 ms: 1.43x slower                                                           |
| Geometric mean       | (ref)                                                                 | 1.06x slower                                                                   |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240926-linux-x86_64-python-2c472d36b776636fb008-3.14.0a0-2c472d3 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-9d28e99 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 7.02 ms                                                               | 7.00 ms: 1.00x faster                                                          |
| python_startup         | 10.5 ms                                                               | 10.6 ms: 1.01x slower                                                          |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240926-linux-x86_64-python-2c472d36b776636fb008-3.14.0a0-2c472d3 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-9d28e99 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_text     | 22.7 ms                                                               | 22.3 ms: 1.02x faster                                                          |
| mako            | 11.1 ms                                                               | 11.3 ms: 1.01x slower                                                          |
| django_template | 34.5 ms                                                               | 35.2 ms: 1.02x slower                                                          |
| genshi_xml      | 50.8 ms                                                               | 54.4 ms: 1.07x slower                                                          |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20240926-linux-x86_64-python-2c472d36b776636fb008-3.14.0a0-2c472d3 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-9d28e99 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pylint                     | 320 ms                                                                | 266 ms: 1.20x faster                                                           |
| regex_dna                  | 237 ms                                                                | 223 ms: 1.07x faster                                                           |
| regex_effbot               | 3.87 ms                                                               | 3.67 ms: 1.06x faster                                                          |
| create_gc_cycles           | 1.73 ms                                                               | 1.68 ms: 1.03x faster                                                          |
| spectral_norm              | 114 ms                                                                | 112 ms: 1.02x faster                                                           |
| genshi_text                | 22.7 ms                                                               | 22.3 ms: 1.02x faster                                                          |
| gc_traversal               | 3.84 ms                                                               | 3.77 ms: 1.02x faster                                                          |
| typing_runtime_protocols   | 160 us                                                                | 157 us: 1.02x faster                                                           |
| raytrace                   | 268 ms                                                                | 264 ms: 1.02x faster                                                           |
| chaos                      | 59.9 ms                                                               | 59.2 ms: 1.01x faster                                                          |
| telco                      | 8.52 ms                                                               | 8.42 ms: 1.01x faster                                                          |
| unpickle                   | 14.7 us                                                               | 14.5 us: 1.01x faster                                                          |
| logging_simple             | 5.74 us                                                               | 5.68 us: 1.01x faster                                                          |
| go                         | 120 ms                                                                | 119 ms: 1.01x faster                                                           |
| richards_super             | 52.8 ms                                                               | 52.4 ms: 1.01x faster                                                          |
| sympy_sum                  | 148 ms                                                                | 147 ms: 1.01x faster                                                           |
| nqueens                    | 80.0 ms                                                               | 79.6 ms: 1.00x faster                                                          |
| unpickle_pure_python       | 216 us                                                                | 215 us: 1.00x faster                                                           |
| asyncio_tcp_ssl            | 1.79 sec                                                              | 1.78 sec: 1.00x faster                                                         |
| python_startup_no_site     | 7.02 ms                                                               | 7.00 ms: 1.00x faster                                                          |
| bench_thread_pool          | 791 us                                                                | 790 us: 1.00x faster                                                           |
| regex_compile              | 128 ms                                                                | 128 ms: 1.00x slower                                                           |
| hexiom                     | 6.29 ms                                                               | 6.31 ms: 1.00x slower                                                          |
| pickle_pure_python         | 303 us                                                                | 305 us: 1.00x slower                                                           |
| pidigits                   | 187 ms                                                                | 187 ms: 1.00x slower                                                           |
| json_loads                 | 26.9 us                                                               | 27.1 us: 1.01x slower                                                          |
| sqlglot_normalize          | 106 ms                                                                | 107 ms: 1.01x slower                                                           |
| pprint_pformat             | 1.46 sec                                                              | 1.47 sec: 1.01x slower                                                         |
| scimark_monte_carlo        | 67.6 ms                                                               | 68.0 ms: 1.01x slower                                                          |
| logging_format             | 6.30 us                                                               | 6.34 us: 1.01x slower                                                          |
| deepcopy                   | 259 us                                                                | 261 us: 1.01x slower                                                           |
| pickle_dict                | 34.6 us                                                               | 34.8 us: 1.01x slower                                                          |
| deepcopy_memo              | 30.4 us                                                               | 30.6 us: 1.01x slower                                                          |
| meteor_contest             | 107 ms                                                                | 108 ms: 1.01x slower                                                           |
| regex_v8                   | 24.3 ms                                                               | 24.5 ms: 1.01x slower                                                          |
| pickle                     | 11.6 us                                                               | 11.7 us: 1.01x slower                                                          |
| python_startup             | 10.5 ms                                                               | 10.6 ms: 1.01x slower                                                          |
| pprint_safe_repr           | 710 ms                                                                | 717 ms: 1.01x slower                                                           |
| pathlib                    | 15.9 ms                                                               | 16.1 ms: 1.01x slower                                                          |
| scimark_fft                | 364 ms                                                                | 368 ms: 1.01x slower                                                           |
| unpickle_list              | 5.16 us                                                               | 5.22 us: 1.01x slower                                                          |
| json_dumps                 | 10.3 ms                                                               | 10.4 ms: 1.01x slower                                                          |
| scimark_sor                | 123 ms                                                                | 125 ms: 1.01x slower                                                           |
| thrift                     | 765 us                                                                | 776 us: 1.01x slower                                                           |
| mako                       | 11.1 ms                                                               | 11.3 ms: 1.01x slower                                                          |
| tornado_http               | 90.1 ms                                                               | 91.5 ms: 1.02x slower                                                          |
| deepcopy_reduce            | 2.66 us                                                               | 2.71 us: 1.02x slower                                                          |
| generators                 | 27.9 ms                                                               | 28.3 ms: 1.02x slower                                                          |
| crypto_pyaes               | 72.2 ms                                                               | 73.4 ms: 1.02x slower                                                          |
| asyncio_tcp                | 472 ms                                                                | 480 ms: 1.02x slower                                                           |
| coverage                   | 85.1 ms                                                               | 86.6 ms: 1.02x slower                                                          |
| sqlglot_optimize           | 53.4 ms                                                               | 54.3 ms: 1.02x slower                                                          |
| django_template            | 34.5 ms                                                               | 35.2 ms: 1.02x slower                                                          |
| scimark_lu                 | 113 ms                                                                | 116 ms: 1.03x slower                                                           |
| pyflate                    | 458 ms                                                                | 474 ms: 1.03x slower                                                           |
| logging_silent             | 101 ns                                                                | 105 ns: 1.04x slower                                                           |
| pickle_list                | 5.14 us                                                               | 5.36 us: 1.04x slower                                                          |
| scimark_sparse_mat_mult    | 4.67 ms                                                               | 4.88 ms: 1.04x slower                                                          |
| docutils                   | 2.65 sec                                                              | 2.77 sec: 1.05x slower                                                         |
| coroutines                 | 22.6 ms                                                               | 23.6 ms: 1.05x slower                                                          |
| async_generators           | 438 ms                                                                | 459 ms: 1.05x slower                                                           |
| sqlglot_transpile          | 1.58 ms                                                               | 1.67 ms: 1.06x slower                                                          |
| 2to3                       | 256 ms                                                                | 272 ms: 1.06x slower                                                           |
| html5lib                   | 63.7 ms                                                               | 68.1 ms: 1.07x slower                                                          |
| genshi_xml                 | 50.8 ms                                                               | 54.4 ms: 1.07x slower                                                          |
| unpack_sequence            | 45.9 ns                                                               | 49.5 ns: 1.08x slower                                                          |
| pycparser                  | 1.13 sec                                                              | 1.22 sec: 1.08x slower                                                         |
| mdp                        | 2.51 sec                                                              | 2.73 sec: 1.09x slower                                                         |
| xml_etree_generate         | 85.3 ms                                                               | 93.0 ms: 1.09x slower                                                          |
| deltablue                  | 3.25 ms                                                               | 3.55 ms: 1.09x slower                                                          |
| sqlglot_parse              | 1.28 ms                                                               | 1.41 ms: 1.10x slower                                                          |
| async_tree_io_tg           | 874 ms                                                                | 966 ms: 1.10x slower                                                           |
| xml_etree_process          | 58.7 ms                                                               | 65.1 ms: 1.11x slower                                                          |
| async_tree_cpu_io_mixed    | 573 ms                                                                | 638 ms: 1.11x slower                                                           |
| async_tree_io              | 883 ms                                                                | 995 ms: 1.13x slower                                                           |
| async_tree_cpu_io_mixed_tg | 559 ms                                                                | 635 ms: 1.13x slower                                                           |
| bpe_tokeniser              | 4.80 sec                                                              | 5.67 sec: 1.18x slower                                                         |
| xml_etree_parse            | 155 ms                                                                | 184 ms: 1.19x slower                                                           |
| async_tree_memoization     | 396 ms                                                                | 489 ms: 1.24x slower                                                           |
| float                      | 77.1 ms                                                               | 97.0 ms: 1.26x slower                                                          |
| async_tree_memoization_tg  | 390 ms                                                                | 498 ms: 1.28x slower                                                           |
| async_tree_none_tg         | 303 ms                                                                | 390 ms: 1.29x slower                                                           |
| async_tree_none            | 317 ms                                                                | 424 ms: 1.34x slower                                                           |
| xml_etree_iterparse        | 104 ms                                                                | 150 ms: 1.43x slower                                                           |
| Geometric mean             | (ref)                                                                 | 1.04x slower                                                                   |

Benchmark hidden because not significant (13): richards, comprehensions, nbody, dulwich_log, asyncio_websockets, bench_mp_pool, sympy_integrate, tomli_loads, fannkuch, sqlite_synth, json, sympy_expand, sympy_str

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.95x