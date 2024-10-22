# Results vs. 3.13.0

- fork: nick-arm
- ref: codecache_rwx
- machine: linux-aarch64
- commit hash: 0442576
- commit date: 2024-10-07
- overall geometric mean: 1.15x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 365 ms: 1.20x slower                                                 |
| docutils       | 2.91 sec                                                 | 3.56 sec: 1.23x slower                                               |
| html5lib       | 64.3 ms                                                  | 70.6 ms: 1.10x slower                                                |
| tornado_http   | 131 ms                                                   | 149 ms: 1.13x slower                                                 |
| Geometric mean | (ref)                                                    | 1.16x slower                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|---------------------------|:--------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg | 649 ms                                                   | 561 ms: 1.16x faster                                                 |
| async_tree_none           | 493 ms                                                   | 442 ms: 1.12x faster                                                 |
| async_tree_none_tg        | 467 ms                                                   | 427 ms: 1.09x faster                                                 |
| async_tree_memoization    | 626 ms                                                   | 585 ms: 1.07x faster                                                 |
| coroutines                | 28.2 ms                                                  | 28.6 ms: 1.01x slower                                                |
| asyncio_websockets        | 656 ms                                                   | 665 ms: 1.01x slower                                                 |
| async_tree_io             | 1.11 sec                                                 | 1.15 sec: 1.04x slower                                               |
| async_generators          | 496 ms                                                   | 517 ms: 1.04x slower                                                 |
| asyncio_tcp_ssl           | 2.18 sec                                                 | 2.28 sec: 1.05x slower                                               |
| async_tree_io_tg          | 1.09 sec                                                 | 1.17 sec: 1.07x slower                                               |
| asyncio_tcp               | 568 ms                                                   | 622 ms: 1.09x slower                                                 |
| Geometric mean            | (ref)                                                    | 1.01x faster                                                         |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 94.4 ms                                                  | 90.2 ms: 1.05x faster                                                |
| nbody          | 114 ms                                                   | 111 ms: 1.03x faster                                                 |
| Geometric mean | (ref)                                                    | 1.02x faster                                                         |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 4.87 ms                                                  | 5.00 ms: 1.03x slower                                                |
| regex_dna      | 246 ms                                                   | 263 ms: 1.07x slower                                                 |
| regex_compile  | 128 ms                                                   | 174 ms: 1.35x slower                                                 |
| Geometric mean | (ref)                                                    | 1.10x slower                                                         |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------------|:--------------------------------------------------------:|:--------------------------------------------------------------------:|
| unpickle             | 20.2 us                                                  | 19.1 us: 1.05x faster                                                |
| unpickle_list        | 6.65 us                                                  | 6.37 us: 1.04x faster                                                |
| xml_etree_generate   | 113 ms                                                   | 109 ms: 1.03x faster                                                 |
| pickle_list          | 5.34 us                                                  | 5.19 us: 1.03x faster                                                |
| json_dumps           | 13.4 ms                                                  | 13.1 ms: 1.02x faster                                                |
| json_loads           | 31.4 us                                                  | 31.1 us: 1.01x faster                                                |
| pickle               | 13.5 us                                                  | 13.8 us: 1.02x slower                                                |
| xml_etree_iterparse  | 147 ms                                                   | 151 ms: 1.03x slower                                                 |
| unpickle_pure_python | 254 us                                                   | 265 us: 1.04x slower                                                 |
| tomli_loads          | 2.53 sec                                                 | 2.64 sec: 1.05x slower                                               |
| pickle_pure_python   | 359 us                                                   | 395 us: 1.10x slower                                                 |
| Geometric mean       | (ref)                                                    | 1.00x slower                                                         |

Benchmark hidden because not significant (3): pickle_dict, xml_etree_process, xml_etree_parse

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|-----------------|:--------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 13.3 ms                                                  | 13.2 ms: 1.01x faster                                                |
| genshi_text     | 27.7 ms                                                  | 33.1 ms: 1.20x slower                                                |
| django_template | 42.3 ms                                                  | 51.2 ms: 1.21x slower                                                |
| genshi_xml      | 60.2 ms                                                  | 78.1 ms: 1.30x slower                                                |
| Geometric mean  | (ref)                                                    | 1.17x slower                                                         |

All benchmarks:
===============

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|---------------------------|:--------------------------------------------------------:|:--------------------------------------------------------------------:|
| deepcopy_memo             | 51.0 us                                                  | 37.4 us: 1.36x faster                                                |
| async_tree_memoization_tg | 649 ms                                                   | 561 ms: 1.16x faster                                                 |
| deepcopy                  | 451 us                                                   | 402 us: 1.12x faster                                                 |
| async_tree_none           | 493 ms                                                   | 442 ms: 1.12x faster                                                 |
| async_tree_none_tg        | 467 ms                                                   | 427 ms: 1.09x faster                                                 |
| async_tree_memoization    | 626 ms                                                   | 585 ms: 1.07x faster                                                 |
| scimark_sor               | 159 ms                                                   | 151 ms: 1.05x faster                                                 |
| unpickle                  | 20.2 us                                                  | 19.1 us: 1.05x faster                                                |
| float                     | 94.4 ms                                                  | 90.2 ms: 1.05x faster                                                |
| unpickle_list             | 6.65 us                                                  | 6.37 us: 1.04x faster                                                |
| telco                     | 9.73 ms                                                  | 9.37 ms: 1.04x faster                                                |
| xml_etree_generate        | 113 ms                                                   | 109 ms: 1.03x faster                                                 |
| deepcopy_reduce           | 4.07 us                                                  | 3.94 us: 1.03x faster                                                |
| nbody                     | 114 ms                                                   | 111 ms: 1.03x faster                                                 |
| pickle_list               | 5.34 us                                                  | 5.19 us: 1.03x faster                                                |
| logging_silent            | 135 ns                                                   | 132 ns: 1.03x faster                                                 |
| pathlib                   | 22.4 ms                                                  | 21.9 ms: 1.02x faster                                                |
| json_dumps                | 13.4 ms                                                  | 13.1 ms: 1.02x faster                                                |
| mako                      | 13.3 ms                                                  | 13.2 ms: 1.01x faster                                                |
| json_loads                | 31.4 us                                                  | 31.1 us: 1.01x faster                                                |
| bpe_tokeniser             | 5.90 sec                                                 | 5.96 sec: 1.01x slower                                               |
| coroutines                | 28.2 ms                                                  | 28.6 ms: 1.01x slower                                                |
| asyncio_websockets        | 656 ms                                                   | 665 ms: 1.01x slower                                                 |
| thrift                    | 946 us                                                   | 959 us: 1.01x slower                                                 |
| pickle                    | 13.5 us                                                  | 13.8 us: 1.02x slower                                                |
| mdp                       | 3.36 sec                                                 | 3.45 sec: 1.02x slower                                               |
| regex_effbot              | 4.87 ms                                                  | 5.00 ms: 1.03x slower                                                |
| xml_etree_iterparse       | 147 ms                                                   | 151 ms: 1.03x slower                                                 |
| logging_format            | 7.83 us                                                  | 8.10 us: 1.03x slower                                                |
| async_tree_io             | 1.11 sec                                                 | 1.15 sec: 1.04x slower                                               |
| scimark_sparse_mat_mult   | 6.58 ms                                                  | 6.83 ms: 1.04x slower                                                |
| unpickle_pure_python      | 254 us                                                   | 265 us: 1.04x slower                                                 |
| async_generators          | 496 ms                                                   | 517 ms: 1.04x slower                                                 |
| tomli_loads               | 2.53 sec                                                 | 2.64 sec: 1.05x slower                                               |
| spectral_norm             | 141 ms                                                   | 147 ms: 1.05x slower                                                 |
| asyncio_tcp_ssl           | 2.18 sec                                                 | 2.28 sec: 1.05x slower                                               |
| scimark_monte_carlo       | 83.8 ms                                                  | 88.2 ms: 1.05x slower                                                |
| richards                  | 53.5 ms                                                  | 56.9 ms: 1.06x slower                                                |
| logging_simple            | 7.04 us                                                  | 7.49 us: 1.06x slower                                                |
| regex_dna                 | 246 ms                                                   | 263 ms: 1.07x slower                                                 |
| typing_runtime_protocols  | 192 us                                                   | 205 us: 1.07x slower                                                 |
| bench_thread_pool         | 1.28 ms                                                  | 1.37 ms: 1.07x slower                                                |
| crypto_pyaes              | 82.7 ms                                                  | 88.6 ms: 1.07x slower                                                |
| create_gc_cycles          | 2.12 ms                                                  | 2.28 ms: 1.07x slower                                                |
| async_tree_io_tg          | 1.09 sec                                                 | 1.17 sec: 1.07x slower                                               |
| meteor_contest            | 113 ms                                                   | 123 ms: 1.08x slower                                                 |
| scimark_lu                | 139 ms                                                   | 151 ms: 1.09x slower                                                 |
| asyncio_tcp               | 568 ms                                                   | 622 ms: 1.09x slower                                                 |
| html5lib                  | 64.3 ms                                                  | 70.6 ms: 1.10x slower                                                |
| pickle_pure_python        | 359 us                                                   | 395 us: 1.10x slower                                                 |
| pyflate                   | 556 ms                                                   | 620 ms: 1.12x slower                                                 |
| fannkuch                  | 452 ms                                                   | 504 ms: 1.12x slower                                                 |
| richards_super            | 60.3 ms                                                  | 67.3 ms: 1.12x slower                                                |
| go                        | 163 ms                                                   | 182 ms: 1.12x slower                                                 |
| deltablue                 | 3.85 ms                                                  | 4.34 ms: 1.13x slower                                                |
| tornado_http              | 131 ms                                                   | 149 ms: 1.13x slower                                                 |
| gc_traversal              | 4.53 ms                                                  | 5.21 ms: 1.15x slower                                                |
| raytrace                  | 298 ms                                                   | 345 ms: 1.16x slower                                                 |
| sqlglot_normalize         | 128 ms                                                   | 149 ms: 1.16x slower                                                 |
| pycparser                 | 1.26 sec                                                 | 1.47 sec: 1.17x slower                                               |
| 2to3                      | 306 ms                                                   | 365 ms: 1.20x slower                                                 |
| genshi_text               | 27.7 ms                                                  | 33.1 ms: 1.20x slower                                                |
| comprehensions            | 20.4 us                                                  | 24.6 us: 1.21x slower                                                |
| django_template           | 42.3 ms                                                  | 51.2 ms: 1.21x slower                                                |
| sqlglot_parse             | 1.38 ms                                                  | 1.68 ms: 1.21x slower                                                |
| sqlglot_optimize          | 62.4 ms                                                  | 76.1 ms: 1.22x slower                                                |
| docutils                  | 2.91 sec                                                 | 3.56 sec: 1.23x slower                                               |
| nqueens                   | 98.7 ms                                                  | 123 ms: 1.24x slower                                                 |
| chaos                     | 68.8 ms                                                  | 86.4 ms: 1.26x slower                                                |
| sympy_expand              | 455 ms                                                   | 573 ms: 1.26x slower                                                 |
| sqlglot_transpile         | 1.73 ms                                                  | 2.21 ms: 1.27x slower                                                |
| genshi_xml                | 60.2 ms                                                  | 78.1 ms: 1.30x slower                                                |
| sympy_str                 | 264 ms                                                   | 346 ms: 1.31x slower                                                 |
| pprint_safe_repr          | 926 ms                                                   | 1.22 sec: 1.32x slower                                               |
| pylint                    | 343 ms                                                   | 459 ms: 1.34x slower                                                 |
| pprint_pformat            | 1.90 sec                                                 | 2.54 sec: 1.34x slower                                               |
| regex_compile             | 128 ms                                                   | 174 ms: 1.35x slower                                                 |
| sympy_integrate           | 21.0 ms                                                  | 28.5 ms: 1.36x slower                                                |
| hexiom                    | 7.13 ms                                                  | 9.90 ms: 1.39x slower                                                |
| sympy_sum                 | 143 ms                                                   | 210 ms: 1.46x slower                                                 |
| generators                | 37.8 ms                                                  | 58.8 ms: 1.56x slower                                                |
| unpack_sequence           | 57.2 ns                                                  | 147 ns: 2.57x slower                                                 |
| bench_mp_pool             | 7.30 ms                                                  | 2.94 sec: 403.27x slower                                             |
| Geometric mean            | (ref)                                                    | 1.15x slower                                                         |

Benchmark hidden because not significant (13): async_tree_cpu_io_mixed, json, python_startup, pickle_dict, xml_etree_process, regex_v8, async_tree_cpu_io_mixed_tg, coverage, scimark_fft, python_startup_no_site, pidigits, sqlite_synth, xml_etree_parse
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20241007-3.14.0a0-0442576-JIT/bm-20241007-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a0-0442576.json: dulwich_log

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.07x