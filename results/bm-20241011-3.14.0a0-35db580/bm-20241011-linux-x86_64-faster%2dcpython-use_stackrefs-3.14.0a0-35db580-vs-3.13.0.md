# Results vs. 3.13.0

- fork: faster-cpython
- ref: use_stackrefs
- machine: linux-x86_64
- commit hash: 35db580
- commit date: 2024-10-11
- overall geometric mean: 1.02x slower
- HPT reliability: 99.67%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241011-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a0-35db580 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 259 ms: 1.02x faster                                                     |
| docutils       | 2.58 sec                                               | 2.66 sec: 1.03x slower                                                   |
| html5lib       | 64.5 ms                                                | 62.5 ms: 1.03x faster                                                    |
| tornado_http   | 91.5 ms                                                | 92.5 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                  | 1.00x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241011-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a0-35db580 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 417 ms: 1.11x faster                                                     |
| async_tree_none            | 354 ms                                                 | 334 ms: 1.06x faster                                                     |
| async_tree_memoization     | 442 ms                                                 | 427 ms: 1.04x faster                                                     |
| asyncio_tcp                | 488 ms                                                 | 483 ms: 1.01x faster                                                     |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.79 sec: 1.00x faster                                                   |
| async_generators           | 433 ms                                                 | 444 ms: 1.03x slower                                                     |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 560 ms: 1.03x slower                                                     |
| async_tree_io_tg           | 825 ms                                                 | 886 ms: 1.07x slower                                                     |
| coroutines                 | 22.5 ms                                                | 25.3 ms: 1.12x slower                                                    |
| async_tree_io              | 843 ms                                                 | 960 ms: 1.14x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.01x slower                                                             |

Benchmark hidden because not significant (3): asyncio_websockets, async_tree_none_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241011-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a0-35db580 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                                     |
| float          | 78.5 ms                                                | 79.4 ms: 1.01x slower                                                    |
| nbody          | 85.7 ms                                                | 93.2 ms: 1.09x slower                                                    |
| Geometric mean | (ref)                                                  | 1.04x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241011-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a0-35db580 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.56 ms: 1.09x faster                                                    |
| regex_v8       | 25.3 ms                                                | 24.3 ms: 1.04x faster                                                    |
| regex_dna      | 220 ms                                                 | 218 ms: 1.01x faster                                                     |
| regex_compile  | 131 ms                                                 | 131 ms: 1.00x faster                                                     |
| Geometric mean | (ref)                                                  | 1.04x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241011-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a0-35db580 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle               | 11.6 us                                                | 11.4 us: 1.01x faster                                                    |
| json_loads           | 27.0 us                                                | 26.7 us: 1.01x faster                                                    |
| xml_etree_generate   | 87.0 ms                                                | 86.6 ms: 1.00x faster                                                    |
| pickle_list          | 5.01 us                                                | 5.06 us: 1.01x slower                                                    |
| unpickle_pure_python | 213 us                                                 | 217 us: 1.02x slower                                                     |
| pickle_dict          | 33.2 us                                                | 34.1 us: 1.03x slower                                                    |
| xml_etree_iterparse  | 102 ms                                                 | 105 ms: 1.03x slower                                                     |
| unpickle             | 14.9 us                                                | 15.4 us: 1.04x slower                                                    |
| pickle_pure_python   | 300 us                                                 | 315 us: 1.05x slower                                                     |
| unpickle_list        | 4.96 us                                                | 5.23 us: 1.05x slower                                                    |
| json_dumps           | 10.4 ms                                                | 11.8 ms: 1.13x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                             |

Benchmark hidden because not significant (3): xml_etree_parse, xml_etree_process, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241011-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a0-35db580 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.99 ms                                                | 7.03 ms: 1.01x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                             |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241011-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a0-35db580 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 22.9 ms                                                | 22.5 ms: 1.02x faster                                                    |
| django_template | 34.4 ms                                                | 35.5 ms: 1.03x slower                                                    |
| mako            | 11.1 ms                                                | 11.8 ms: 1.06x slower                                                    |
| Geometric mean  | (ref)                                                  | 1.02x slower                                                             |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241011-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a0-35db580 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| deepcopy                   | 352 us                                                 | 266 us: 1.32x faster                                                     |
| deepcopy_memo              | 38.0 us                                                | 31.2 us: 1.22x faster                                                    |
| go                         | 142 ms                                                 | 121 ms: 1.17x faster                                                     |
| deepcopy_reduce            | 3.17 us                                                | 2.78 us: 1.14x faster                                                    |
| async_tree_memoization_tg  | 465 ms                                                 | 417 ms: 1.11x faster                                                     |
| regex_effbot               | 3.88 ms                                                | 3.56 ms: 1.09x faster                                                    |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.70 ms: 1.07x faster                                                    |
| async_tree_none            | 354 ms                                                 | 334 ms: 1.06x faster                                                     |
| mdp                        | 2.74 sec                                               | 2.61 sec: 1.05x faster                                                   |
| telco                      | 8.45 ms                                                | 8.06 ms: 1.05x faster                                                    |
| pathlib                    | 17.1 ms                                                | 16.3 ms: 1.04x faster                                                    |
| regex_v8                   | 25.3 ms                                                | 24.3 ms: 1.04x faster                                                    |
| async_tree_memoization     | 442 ms                                                 | 427 ms: 1.04x faster                                                     |
| html5lib                   | 64.5 ms                                                | 62.5 ms: 1.03x faster                                                    |
| 2to3                       | 265 ms                                                 | 259 ms: 1.02x faster                                                     |
| scimark_lu                 | 115 ms                                                 | 112 ms: 1.02x faster                                                     |
| json                       | 5.20 ms                                                | 5.09 ms: 1.02x faster                                                    |
| scimark_fft                | 369 ms                                                 | 361 ms: 1.02x faster                                                     |
| richards                   | 48.1 ms                                                | 47.3 ms: 1.02x faster                                                    |
| genshi_text                | 22.9 ms                                                | 22.5 ms: 1.02x faster                                                    |
| pickle                     | 11.6 us                                                | 11.4 us: 1.01x faster                                                    |
| spectral_norm              | 115 ms                                                 | 114 ms: 1.01x faster                                                     |
| asyncio_tcp                | 488 ms                                                 | 483 ms: 1.01x faster                                                     |
| gc_traversal               | 3.81 ms                                                | 3.77 ms: 1.01x faster                                                    |
| json_loads                 | 27.0 us                                                | 26.7 us: 1.01x faster                                                    |
| richards_super             | 54.4 ms                                                | 54.0 ms: 1.01x faster                                                    |
| regex_dna                  | 220 ms                                                 | 218 ms: 1.01x faster                                                     |
| regex_compile              | 131 ms                                                 | 131 ms: 1.00x faster                                                     |
| xml_etree_generate         | 87.0 ms                                                | 86.6 ms: 1.00x faster                                                    |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.79 sec: 1.00x faster                                                   |
| meteor_contest             | 108 ms                                                 | 108 ms: 1.00x slower                                                     |
| sympy_sum                  | 150 ms                                                 | 151 ms: 1.01x slower                                                     |
| python_startup_no_site     | 6.99 ms                                                | 7.03 ms: 1.01x slower                                                    |
| thrift                     | 796 us                                                 | 802 us: 1.01x slower                                                     |
| pidigits                   | 186 ms                                                 | 188 ms: 1.01x slower                                                     |
| tornado_http               | 91.5 ms                                                | 92.5 ms: 1.01x slower                                                    |
| sympy_str                  | 274 ms                                                 | 276 ms: 1.01x slower                                                     |
| coverage                   | 83.7 ms                                                | 84.7 ms: 1.01x slower                                                    |
| pickle_list                | 5.01 us                                                | 5.06 us: 1.01x slower                                                    |
| float                      | 78.5 ms                                                | 79.4 ms: 1.01x slower                                                    |
| generators                 | 28.8 ms                                                | 29.2 ms: 1.01x slower                                                    |
| sympy_integrate            | 19.9 ms                                                | 20.2 ms: 1.01x slower                                                    |
| unpickle_pure_python       | 213 us                                                 | 217 us: 1.02x slower                                                     |
| nqueens                    | 80.6 ms                                                | 82.0 ms: 1.02x slower                                                    |
| sqlglot_normalize          | 107 ms                                                 | 109 ms: 1.02x slower                                                     |
| sqlglot_optimize           | 53.9 ms                                                | 54.9 ms: 1.02x slower                                                    |
| bpe_tokeniser              | 4.69 sec                                               | 4.79 sec: 1.02x slower                                                   |
| raytrace                   | 262 ms                                                 | 267 ms: 1.02x slower                                                     |
| sympy_expand               | 462 ms                                                 | 472 ms: 1.02x slower                                                     |
| logging_format             | 6.25 us                                                | 6.40 us: 1.02x slower                                                    |
| logging_simple             | 5.66 us                                                | 5.80 us: 1.02x slower                                                    |
| async_generators           | 433 ms                                                 | 444 ms: 1.03x slower                                                     |
| pprint_safe_repr           | 744 ms                                                 | 763 ms: 1.03x slower                                                     |
| pickle_dict                | 33.2 us                                                | 34.1 us: 1.03x slower                                                    |
| docutils                   | 2.58 sec                                               | 2.66 sec: 1.03x slower                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 560 ms: 1.03x slower                                                     |
| xml_etree_iterparse        | 102 ms                                                 | 105 ms: 1.03x slower                                                     |
| typing_runtime_protocols   | 159 us                                                 | 164 us: 1.03x slower                                                     |
| hexiom                     | 6.13 ms                                                | 6.32 ms: 1.03x slower                                                    |
| django_template            | 34.4 ms                                                | 35.5 ms: 1.03x slower                                                    |
| sqlglot_transpile          | 1.57 ms                                                | 1.63 ms: 1.03x slower                                                    |
| crypto_pyaes               | 73.0 ms                                                | 75.5 ms: 1.03x slower                                                    |
| unpickle                   | 14.9 us                                                | 15.4 us: 1.04x slower                                                    |
| pprint_pformat             | 1.51 sec                                               | 1.57 sec: 1.04x slower                                                   |
| dulwich_log                | 63.0 ms                                                | 65.4 ms: 1.04x slower                                                    |
| scimark_monte_carlo        | 66.3 ms                                                | 69.0 ms: 1.04x slower                                                    |
| sqlglot_parse              | 1.27 ms                                                | 1.32 ms: 1.04x slower                                                    |
| comprehensions             | 16.4 us                                                | 17.1 us: 1.04x slower                                                    |
| deltablue                  | 3.15 ms                                                | 3.29 ms: 1.04x slower                                                    |
| pickle_pure_python         | 300 us                                                 | 315 us: 1.05x slower                                                     |
| bench_thread_pool          | 815 us                                                 | 858 us: 1.05x slower                                                     |
| unpickle_list              | 4.96 us                                                | 5.23 us: 1.05x slower                                                    |
| chaos                      | 58.4 ms                                                | 62.1 ms: 1.06x slower                                                    |
| mako                       | 11.1 ms                                                | 11.8 ms: 1.06x slower                                                    |
| pyflate                    | 460 ms                                                 | 490 ms: 1.07x slower                                                     |
| scimark_sor                | 122 ms                                                 | 131 ms: 1.07x slower                                                     |
| async_tree_io_tg           | 825 ms                                                 | 886 ms: 1.07x slower                                                     |
| nbody                      | 85.7 ms                                                | 93.2 ms: 1.09x slower                                                    |
| fannkuch                   | 381 ms                                                 | 418 ms: 1.10x slower                                                     |
| unpack_sequence            | 42.4 ns                                                | 46.6 ns: 1.10x slower                                                    |
| create_gc_cycles           | 1.61 ms                                                | 1.78 ms: 1.10x slower                                                    |
| coroutines                 | 22.5 ms                                                | 25.3 ms: 1.12x slower                                                    |
| json_dumps                 | 10.4 ms                                                | 11.8 ms: 1.13x slower                                                    |
| async_tree_io              | 843 ms                                                 | 960 ms: 1.14x slower                                                     |
| bench_mp_pool              | 24.0 ms                                                | 56.2 ms: 2.34x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.02x slower                                                             |

Benchmark hidden because not significant (12): genshi_xml, xml_etree_parse, sqlite_synth, xml_etree_process, asyncio_websockets, python_startup, async_tree_none_tg, pycparser, tomli_loads, logging_silent, async_tree_cpu_io_mixed, pylint
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 99.67% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x