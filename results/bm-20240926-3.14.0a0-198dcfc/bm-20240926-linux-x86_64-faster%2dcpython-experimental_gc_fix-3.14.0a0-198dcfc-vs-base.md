# Results vs. base

- fork: faster-cpython
- ref: experimental_gc_fix
- machine: linux-x86_64
- commit hash: 198dcfc
- commit date: 2024-09-26
- overall geometric mean: 1.03x slower
- HPT reliability: 97.59%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.96x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240926-linux-x86_64-python-2c472d36b776636fb008-3.14.0a0-2c472d3 | bm-20240926-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-198dcfc |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 256 ms                                                                | 271 ms: 1.06x slower                                                           |
| docutils       | 2.65 sec                                                              | 2.70 sec: 1.02x slower                                                         |
| html5lib       | 63.7 ms                                                               | 68.1 ms: 1.07x slower                                                          |
| tornado_http   | 90.1 ms                                                               | 91.8 ms: 1.02x slower                                                          |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240926-linux-x86_64-python-2c472d36b776636fb008-3.14.0a0-2c472d3 | bm-20240926-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-198dcfc |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 1.79 sec                                                              | 1.78 sec: 1.00x faster                                                         |
| asyncio_tcp                | 472 ms                                                                | 480 ms: 1.02x slower                                                           |
| coroutines                 | 22.6 ms                                                               | 23.0 ms: 1.02x slower                                                          |
| async_generators           | 438 ms                                                                | 455 ms: 1.04x slower                                                           |
| async_tree_io_tg           | 874 ms                                                                | 959 ms: 1.10x slower                                                           |
| async_tree_io              | 883 ms                                                                | 987 ms: 1.12x slower                                                           |
| async_tree_cpu_io_mixed_tg | 559 ms                                                                | 627 ms: 1.12x slower                                                           |
| async_tree_cpu_io_mixed    | 573 ms                                                                | 644 ms: 1.12x slower                                                           |
| async_tree_memoization     | 396 ms                                                                | 481 ms: 1.22x slower                                                           |
| async_tree_none_tg         | 303 ms                                                                | 386 ms: 1.27x slower                                                           |
| async_tree_memoization_tg  | 390 ms                                                                | 498 ms: 1.28x slower                                                           |
| async_tree_none            | 317 ms                                                                | 424 ms: 1.34x slower                                                           |
| Geometric mean             | (ref)                                                                 | 1.12x slower                                                                   |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240926-linux-x86_64-python-2c472d36b776636fb008-3.14.0a0-2c472d3 | bm-20240926-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-198dcfc |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 88.0 ms                                                               | 86.4 ms: 1.02x faster                                                          |
| pidigits       | 187 ms                                                                | 187 ms: 1.00x slower                                                           |
| float          | 77.1 ms                                                               | 95.9 ms: 1.24x slower                                                          |
| Geometric mean | (ref)                                                                 | 1.07x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240926-linux-x86_64-python-2c472d36b776636fb008-3.14.0a0-2c472d3 | bm-20240926-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-198dcfc |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 237 ms                                                                | 222 ms: 1.07x faster                                                           |
| regex_effbot   | 3.87 ms                                                               | 3.64 ms: 1.07x faster                                                          |
| regex_v8       | 24.3 ms                                                               | 25.1 ms: 1.03x slower                                                          |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                                   |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240926-linux-x86_64-python-2c472d36b776636fb008-3.14.0a0-2c472d3 | bm-20240926-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-198dcfc |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| unpickle_pure_python | 216 us                                                                | 211 us: 1.02x faster                                                           |
| tomli_loads          | 2.09 sec                                                              | 2.07 sec: 1.01x faster                                                         |
| pickle_dict          | 34.6 us                                                               | 34.4 us: 1.01x faster                                                          |
| pickle               | 11.6 us                                                               | 11.6 us: 1.00x faster                                                          |
| json_dumps           | 10.3 ms                                                               | 10.4 ms: 1.01x slower                                                          |
| json_loads           | 26.9 us                                                               | 27.2 us: 1.01x slower                                                          |
| unpickle_list        | 5.16 us                                                               | 5.25 us: 1.02x slower                                                          |
| xml_etree_generate   | 85.3 ms                                                               | 91.0 ms: 1.07x slower                                                          |
| xml_etree_parse      | 155 ms                                                                | 171 ms: 1.11x slower                                                           |
| xml_etree_process    | 58.7 ms                                                               | 65.2 ms: 1.11x slower                                                          |
| xml_etree_iterparse  | 104 ms                                                                | 157 ms: 1.51x slower                                                           |
| Geometric mean       | (ref)                                                                 | 1.05x slower                                                                   |

Benchmark hidden because not significant (3): unpickle, pickle_pure_python, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240926-linux-x86_64-python-2c472d36b776636fb008-3.14.0a0-2c472d3 | bm-20240926-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-198dcfc |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 7.02 ms                                                               | 7.01 ms: 1.00x faster                                                          |
| python_startup         | 10.5 ms                                                               | 10.7 ms: 1.01x slower                                                          |
| Geometric mean         | (ref)                                                                 | 1.01x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240926-linux-x86_64-python-2c472d36b776636fb008-3.14.0a0-2c472d3 | bm-20240926-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-198dcfc |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_text     | 22.7 ms                                                               | 22.1 ms: 1.03x faster                                                          |
| django_template | 34.5 ms                                                               | 34.2 ms: 1.01x faster                                                          |
| mako            | 11.1 ms                                                               | 11.2 ms: 1.01x slower                                                          |
| genshi_xml      | 50.8 ms                                                               | 54.5 ms: 1.07x slower                                                          |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20240926-linux-x86_64-python-2c472d36b776636fb008-3.14.0a0-2c472d3 | bm-20240926-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-198dcfc |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| gc_traversal               | 3.84 ms                                                               | 3.53 ms: 1.09x faster                                                          |
| regex_dna                  | 237 ms                                                                | 222 ms: 1.07x faster                                                           |
| regex_effbot               | 3.87 ms                                                               | 3.64 ms: 1.07x faster                                                          |
| deepcopy_memo              | 30.4 us                                                               | 29.6 us: 1.03x faster                                                          |
| genshi_text                | 22.7 ms                                                               | 22.1 ms: 1.03x faster                                                          |
| telco                      | 8.52 ms                                                               | 8.30 ms: 1.03x faster                                                          |
| raytrace                   | 268 ms                                                                | 261 ms: 1.03x faster                                                           |
| go                         | 120 ms                                                                | 117 ms: 1.02x faster                                                           |
| chaos                      | 59.9 ms                                                               | 58.5 ms: 1.02x faster                                                          |
| logging_simple             | 5.74 us                                                               | 5.61 us: 1.02x faster                                                          |
| unpickle_pure_python       | 216 us                                                                | 211 us: 1.02x faster                                                           |
| spectral_norm              | 114 ms                                                                | 112 ms: 1.02x faster                                                           |
| nbody                      | 88.0 ms                                                               | 86.4 ms: 1.02x faster                                                          |
| hexiom                     | 6.29 ms                                                               | 6.18 ms: 1.02x faster                                                          |
| richards_super             | 52.8 ms                                                               | 51.9 ms: 1.02x faster                                                          |
| scimark_fft                | 364 ms                                                                | 358 ms: 1.02x faster                                                           |
| logging_format             | 6.30 us                                                               | 6.20 us: 1.02x faster                                                          |
| richards                   | 46.5 ms                                                               | 45.9 ms: 1.01x faster                                                          |
| deepcopy                   | 259 us                                                                | 256 us: 1.01x faster                                                           |
| tomli_loads                | 2.09 sec                                                              | 2.07 sec: 1.01x faster                                                         |
| create_gc_cycles           | 1.73 ms                                                               | 1.71 ms: 1.01x faster                                                          |
| scimark_monte_carlo        | 67.6 ms                                                               | 66.8 ms: 1.01x faster                                                          |
| unpack_sequence            | 45.9 ns                                                               | 45.5 ns: 1.01x faster                                                          |
| django_template            | 34.5 ms                                                               | 34.2 ms: 1.01x faster                                                          |
| sympy_integrate            | 19.6 ms                                                               | 19.5 ms: 1.01x faster                                                          |
| generators                 | 27.9 ms                                                               | 27.6 ms: 1.01x faster                                                          |
| dulwich_log                | 64.9 ms                                                               | 64.5 ms: 1.01x faster                                                          |
| nqueens                    | 80.0 ms                                                               | 79.5 ms: 1.01x faster                                                          |
| sympy_expand               | 455 ms                                                                | 453 ms: 1.01x faster                                                           |
| pickle_dict                | 34.6 us                                                               | 34.4 us: 1.01x faster                                                          |
| pickle                     | 11.6 us                                                               | 11.6 us: 1.00x faster                                                          |
| crypto_pyaes               | 72.2 ms                                                               | 71.9 ms: 1.00x faster                                                          |
| sqlglot_normalize          | 106 ms                                                                | 106 ms: 1.00x faster                                                           |
| meteor_contest             | 107 ms                                                                | 107 ms: 1.00x faster                                                           |
| comprehensions             | 16.6 us                                                               | 16.5 us: 1.00x faster                                                          |
| asyncio_tcp_ssl            | 1.79 sec                                                              | 1.78 sec: 1.00x faster                                                         |
| bench_thread_pool          | 791 us                                                                | 790 us: 1.00x faster                                                           |
| python_startup_no_site     | 7.02 ms                                                               | 7.01 ms: 1.00x faster                                                          |
| pidigits                   | 187 ms                                                                | 187 ms: 1.00x slower                                                           |
| json_dumps                 | 10.3 ms                                                               | 10.4 ms: 1.01x slower                                                          |
| mdp                        | 2.51 sec                                                              | 2.53 sec: 1.01x slower                                                         |
| mako                       | 11.1 ms                                                               | 11.2 ms: 1.01x slower                                                          |
| json_loads                 | 26.9 us                                                               | 27.2 us: 1.01x slower                                                          |
| json                       | 5.11 ms                                                               | 5.17 ms: 1.01x slower                                                          |
| pathlib                    | 15.9 ms                                                               | 16.1 ms: 1.01x slower                                                          |
| deltablue                  | 3.25 ms                                                               | 3.29 ms: 1.01x slower                                                          |
| python_startup             | 10.5 ms                                                               | 10.7 ms: 1.01x slower                                                          |
| sqlglot_optimize           | 53.4 ms                                                               | 54.1 ms: 1.01x slower                                                          |
| thrift                     | 765 us                                                                | 776 us: 1.02x slower                                                           |
| scimark_sparse_mat_mult    | 4.67 ms                                                               | 4.74 ms: 1.02x slower                                                          |
| docutils                   | 2.65 sec                                                              | 2.70 sec: 1.02x slower                                                         |
| asyncio_tcp                | 472 ms                                                                | 480 ms: 1.02x slower                                                           |
| unpickle_list              | 5.16 us                                                               | 5.25 us: 1.02x slower                                                          |
| tornado_http               | 90.1 ms                                                               | 91.8 ms: 1.02x slower                                                          |
| coroutines                 | 22.6 ms                                                               | 23.0 ms: 1.02x slower                                                          |
| sqlglot_transpile          | 1.58 ms                                                               | 1.62 ms: 1.02x slower                                                          |
| sqlglot_parse              | 1.28 ms                                                               | 1.31 ms: 1.02x slower                                                          |
| pyflate                    | 458 ms                                                                | 472 ms: 1.03x slower                                                           |
| regex_v8                   | 24.3 ms                                                               | 25.1 ms: 1.03x slower                                                          |
| async_generators           | 438 ms                                                                | 455 ms: 1.04x slower                                                           |
| 2to3                       | 256 ms                                                                | 271 ms: 1.06x slower                                                           |
| xml_etree_generate         | 85.3 ms                                                               | 91.0 ms: 1.07x slower                                                          |
| html5lib                   | 63.7 ms                                                               | 68.1 ms: 1.07x slower                                                          |
| genshi_xml                 | 50.8 ms                                                               | 54.5 ms: 1.07x slower                                                          |
| pycparser                  | 1.13 sec                                                              | 1.22 sec: 1.08x slower                                                         |
| async_tree_io_tg           | 874 ms                                                                | 959 ms: 1.10x slower                                                           |
| xml_etree_parse            | 155 ms                                                                | 171 ms: 1.11x slower                                                           |
| xml_etree_process          | 58.7 ms                                                               | 65.2 ms: 1.11x slower                                                          |
| async_tree_io              | 883 ms                                                                | 987 ms: 1.12x slower                                                           |
| async_tree_cpu_io_mixed_tg | 559 ms                                                                | 627 ms: 1.12x slower                                                           |
| async_tree_cpu_io_mixed    | 573 ms                                                                | 644 ms: 1.12x slower                                                           |
| bpe_tokeniser              | 4.80 sec                                                              | 5.76 sec: 1.20x slower                                                         |
| async_tree_memoization     | 396 ms                                                                | 481 ms: 1.22x slower                                                           |
| float                      | 77.1 ms                                                               | 95.9 ms: 1.24x slower                                                          |
| async_tree_none_tg         | 303 ms                                                                | 386 ms: 1.27x slower                                                           |
| async_tree_memoization_tg  | 390 ms                                                                | 498 ms: 1.28x slower                                                           |
| async_tree_none            | 317 ms                                                                | 424 ms: 1.34x slower                                                           |
| xml_etree_iterparse        | 104 ms                                                                | 157 ms: 1.51x slower                                                           |
| Geometric mean             | (ref)                                                                 | 1.03x slower                                                                   |

Benchmark hidden because not significant (19): deepcopy_reduce, pprint_safe_repr, unpickle, pprint_pformat, sympy_sum, pylint, pickle_pure_python, pickle_list, logging_silent, bench_mp_pool, typing_runtime_protocols, scimark_sor, asyncio_websockets, sympy_str, regex_compile, fannkuch, sqlite_synth, coverage, scimark_lu

# HPT report

- Reliability score: 97.59% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.96x