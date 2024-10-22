# Results vs. 3.13.0

- fork: python
- ref: 760872efecb95017db8e
- machine: darwin-arm64
- commit hash: 760872e
- commit date: 2024-10-16
- overall geometric mean: 1.02x faster
- HPT reliability: 99.84%
- HPT 99th percentile: 1.00x faster
- Memory change: 6.75x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-darwin-arm64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 178 ms                                                 | 183 ms: 1.03x slower                                                   |
| docutils       | 1.44 sec                                               | 1.57 sec: 1.09x slower                                                 |
| html5lib       | 36.6 ms                                                | 33.9 ms: 1.08x faster                                                  |
| Geometric mean | (ref)                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-darwin-arm64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg        | 291 ms                                                 | 234 ms: 1.24x faster                                                   |
| coroutines                       | 19.8 ms                                                | 16.6 ms: 1.19x faster                                                  |
| async_tree_eager_tg              | 48.4 ms                                                | 42.9 ms: 1.13x faster                                                  |
| async_tree_eager                 | 70.5 ms                                                | 62.8 ms: 1.12x faster                                                  |
| async_tree_eager_memoization     | 169 ms                                                 | 152 ms: 1.11x faster                                                   |
| async_tree_memoization           | 270 ms                                                 | 243 ms: 1.11x faster                                                   |
| async_tree_none                  | 212 ms                                                 | 197 ms: 1.07x faster                                                   |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 130 ms: 1.07x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 336 ms: 1.04x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 362 ms: 1.03x faster                                                   |
| async_generators                 | 294 ms                                                 | 291 ms: 1.01x faster                                                   |
| asyncio_websockets               | 241 ms                                                 | 242 ms: 1.00x slower                                                   |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.29 sec: 1.02x slower                                                 |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 468 ms: 1.05x slower                                                   |
| async_tree_none_tg               | 198 ms                                                 | 212 ms: 1.07x slower                                                   |
| async_tree_io                    | 507 ms                                                 | 579 ms: 1.14x slower                                                   |
| async_tree_io_tg                 | 500 ms                                                 | 610 ms: 1.22x slower                                                   |
| async_tree_eager_io              | 513 ms                                                 | 667 ms: 1.30x slower                                                   |
| async_tree_eager_io_tg           | 477 ms                                                 | 712 ms: 1.49x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (2): asyncio_tcp, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-darwin-arm64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 56.2 ms                                                | 48.3 ms: 1.16x faster                                                  |
| nbody          | 73.9 ms                                                | 65.3 ms: 1.13x faster                                                  |
| Geometric mean | (ref)                                                  | 1.10x faster                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-darwin-arm64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 78.5 ms                                                | 75.0 ms: 1.05x faster                                                  |
| regex_effbot   | 2.63 ms                                                | 2.60 ms: 1.01x faster                                                  |
| regex_v8       | 16.9 ms                                                | 16.8 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-darwin-arm64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 1.56 sec                                               | 1.24 sec: 1.25x faster                                                 |
| unpickle_pure_python | 163 us                                                 | 132 us: 1.24x faster                                                   |
| pickle_pure_python   | 213 us                                                 | 178 us: 1.19x faster                                                   |
| xml_etree_process    | 40.9 ms                                                | 34.5 ms: 1.19x faster                                                  |
| xml_etree_generate   | 56.6 ms                                                | 50.3 ms: 1.13x faster                                                  |
| json_loads           | 16.9 us                                                | 16.5 us: 1.02x faster                                                  |
| xml_etree_iterparse  | 74.2 ms                                                | 72.5 ms: 1.02x faster                                                  |
| xml_etree_parse      | 109 ms                                                 | 106 ms: 1.02x faster                                                   |
| pickle_list          | 2.99 us                                                | 2.94 us: 1.02x faster                                                  |
| pickle               | 7.36 us                                                | 7.30 us: 1.01x faster                                                  |
| unpickle             | 9.15 us                                                | 9.08 us: 1.01x faster                                                  |
| pickle_dict          | 18.2 us                                                | 18.1 us: 1.00x faster                                                  |
| unpickle_list        | 2.93 us                                                | 2.97 us: 1.02x slower                                                  |
| json_dumps           | 6.56 ms                                                | 7.12 ms: 1.08x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-darwin-arm64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 13.7 ms                                                | 14.6 ms: 1.07x slower                                                  |
| python_startup         | 17.0 ms                                                | 18.9 ms: 1.11x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.09x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-darwin-arm64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 7.68 ms                                                | 6.47 ms: 1.19x faster                                                  |
| genshi_text     | 16.9 ms                                                | 16.6 ms: 1.01x faster                                                  |
| django_template | 22.2 ms                                                | 22.6 ms: 1.02x slower                                                  |
| genshi_xml      | 34.4 ms                                                | 42.7 ms: 1.24x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-darwin-arm64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deepcopy_memo                    | 27.2 us                                                | 16.8 us: 1.62x faster                                                  |
| deepcopy                         | 232 us                                                 | 152 us: 1.53x faster                                                   |
| deepcopy_reduce                  | 2.06 us                                                | 1.50 us: 1.37x faster                                                  |
| tomli_loads                      | 1.56 sec                                               | 1.24 sec: 1.25x faster                                                 |
| generators                       | 31.5 ms                                                | 25.2 ms: 1.25x faster                                                  |
| async_tree_memoization_tg        | 291 ms                                                 | 234 ms: 1.24x faster                                                   |
| unpickle_pure_python             | 163 us                                                 | 132 us: 1.24x faster                                                   |
| scimark_sor                      | 106 ms                                                 | 86.2 ms: 1.23x faster                                                  |
| pickle_pure_python               | 213 us                                                 | 178 us: 1.19x faster                                                   |
| coroutines                       | 19.8 ms                                                | 16.6 ms: 1.19x faster                                                  |
| scimark_lu                       | 76.5 ms                                                | 64.4 ms: 1.19x faster                                                  |
| mako                             | 7.68 ms                                                | 6.47 ms: 1.19x faster                                                  |
| xml_etree_process                | 40.9 ms                                                | 34.5 ms: 1.19x faster                                                  |
| go                               | 115 ms                                                 | 98.0 ms: 1.17x faster                                                  |
| float                            | 56.2 ms                                                | 48.3 ms: 1.16x faster                                                  |
| logging_simple                   | 3.57 us                                                | 3.13 us: 1.14x faster                                                  |
| logging_format                   | 3.85 us                                                | 3.40 us: 1.13x faster                                                  |
| nbody                            | 73.9 ms                                                | 65.3 ms: 1.13x faster                                                  |
| async_tree_eager_tg              | 48.4 ms                                                | 42.9 ms: 1.13x faster                                                  |
| xml_etree_generate               | 56.6 ms                                                | 50.3 ms: 1.13x faster                                                  |
| async_tree_eager                 | 70.5 ms                                                | 62.8 ms: 1.12x faster                                                  |
| spectral_norm                    | 77.3 ms                                                | 69.3 ms: 1.11x faster                                                  |
| thrift                           | 466 us                                                 | 418 us: 1.11x faster                                                   |
| async_tree_eager_memoization     | 169 ms                                                 | 152 ms: 1.11x faster                                                   |
| async_tree_memoization           | 270 ms                                                 | 243 ms: 1.11x faster                                                   |
| scimark_monte_carlo              | 50.4 ms                                                | 45.6 ms: 1.11x faster                                                  |
| deltablue                        | 2.68 ms                                                | 2.43 ms: 1.10x faster                                                  |
| raytrace                         | 182 ms                                                 | 167 ms: 1.09x faster                                                   |
| html5lib                         | 36.6 ms                                                | 33.9 ms: 1.08x faster                                                  |
| pprint_pformat                   | 1.08 sec                                               | 998 ms: 1.08x faster                                                   |
| nqueens                          | 62.9 ms                                                | 58.4 ms: 1.08x faster                                                  |
| pyflate                          | 351 ms                                                 | 326 ms: 1.08x faster                                                   |
| async_tree_none                  | 212 ms                                                 | 197 ms: 1.07x faster                                                   |
| bench_thread_pool                | 506 us                                                 | 472 us: 1.07x faster                                                   |
| fannkuch                         | 282 ms                                                 | 264 ms: 1.07x faster                                                   |
| pprint_safe_repr                 | 531 ms                                                 | 497 ms: 1.07x faster                                                   |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 130 ms: 1.07x faster                                                   |
| typing_runtime_protocols         | 101 us                                                 | 94.8 us: 1.07x faster                                                  |
| bpe_tokeniser                    | 3.24 sec                                               | 3.04 sec: 1.07x faster                                                 |
| richards                         | 35.4 ms                                                | 33.4 ms: 1.06x faster                                                  |
| telco                            | 4.80 ms                                                | 4.54 ms: 1.06x faster                                                  |
| richards_super                   | 39.1 ms                                                | 37.1 ms: 1.06x faster                                                  |
| scimark_fft                      | 201 ms                                                 | 190 ms: 1.05x faster                                                   |
| coverage                         | 46.1 ms                                                | 43.9 ms: 1.05x faster                                                  |
| regex_compile                    | 78.5 ms                                                | 75.0 ms: 1.05x faster                                                  |
| pycparser                        | 706 ms                                                 | 678 ms: 1.04x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 336 ms: 1.04x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 362 ms: 1.03x faster                                                   |
| sqlglot_normalize                | 189 ms                                                 | 182 ms: 1.03x faster                                                   |
| json                             | 2.94 ms                                                | 2.87 ms: 1.02x faster                                                  |
| json_loads                       | 16.9 us                                                | 16.5 us: 1.02x faster                                                  |
| xml_etree_iterparse              | 74.2 ms                                                | 72.5 ms: 1.02x faster                                                  |
| pathlib                          | 22.8 ms                                                | 22.3 ms: 1.02x faster                                                  |
| xml_etree_parse                  | 109 ms                                                 | 106 ms: 1.02x faster                                                   |
| pickle_list                      | 2.99 us                                                | 2.94 us: 1.02x faster                                                  |
| genshi_text                      | 16.9 ms                                                | 16.6 ms: 1.01x faster                                                  |
| async_generators                 | 294 ms                                                 | 291 ms: 1.01x faster                                                   |
| regex_effbot                     | 2.63 ms                                                | 2.60 ms: 1.01x faster                                                  |
| pickle                           | 7.36 us                                                | 7.30 us: 1.01x faster                                                  |
| unpickle                         | 9.15 us                                                | 9.08 us: 1.01x faster                                                  |
| sympy_expand                     | 246 ms                                                 | 245 ms: 1.01x faster                                                   |
| regex_v8                         | 16.9 ms                                                | 16.8 ms: 1.01x faster                                                  |
| sqlite_synth                     | 1.54 us                                                | 1.54 us: 1.01x faster                                                  |
| crypto_pyaes                     | 54.0 ms                                                | 53.9 ms: 1.00x faster                                                  |
| pickle_dict                      | 18.2 us                                                | 18.1 us: 1.00x faster                                                  |
| asyncio_websockets               | 241 ms                                                 | 242 ms: 1.00x slower                                                   |
| chaos                            | 41.3 ms                                                | 41.4 ms: 1.00x slower                                                  |
| hexiom                           | 4.85 ms                                                | 4.92 ms: 1.01x slower                                                  |
| unpickle_list                    | 2.93 us                                                | 2.97 us: 1.02x slower                                                  |
| django_template                  | 22.2 ms                                                | 22.6 ms: 1.02x slower                                                  |
| meteor_contest                   | 73.8 ms                                                | 75.2 ms: 1.02x slower                                                  |
| sqlglot_parse                    | 856 us                                                 | 875 us: 1.02x slower                                                   |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.29 sec: 1.02x slower                                                 |
| mdp                              | 1.50 sec                                               | 1.54 sec: 1.02x slower                                                 |
| 2to3                             | 178 ms                                                 | 183 ms: 1.03x slower                                                   |
| sqlglot_transpile                | 1.02 ms                                                | 1.06 ms: 1.03x slower                                                  |
| sympy_str                        | 145 ms                                                 | 151 ms: 1.04x slower                                                   |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 468 ms: 1.05x slower                                                   |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 3.14 ms: 1.05x slower                                                  |
| sqlglot_optimize                 | 34.9 ms                                                | 36.8 ms: 1.05x slower                                                  |
| sympy_sum                        | 75.6 ms                                                | 79.7 ms: 1.05x slower                                                  |
| python_startup_no_site           | 13.7 ms                                                | 14.6 ms: 1.07x slower                                                  |
| async_tree_none_tg               | 198 ms                                                 | 212 ms: 1.07x slower                                                   |
| comprehensions                   | 12.2 us                                                | 13.0 us: 1.07x slower                                                  |
| json_dumps                       | 6.56 ms                                                | 7.12 ms: 1.08x slower                                                  |
| docutils                         | 1.44 sec                                               | 1.57 sec: 1.09x slower                                                 |
| sympy_integrate                  | 11.3 ms                                                | 12.5 ms: 1.10x slower                                                  |
| python_startup                   | 17.0 ms                                                | 18.9 ms: 1.11x slower                                                  |
| async_tree_io                    | 507 ms                                                 | 579 ms: 1.14x slower                                                   |
| pylint                           | 181 ms                                                 | 212 ms: 1.17x slower                                                   |
| gc_traversal                     | 2.48 ms                                                | 2.96 ms: 1.19x slower                                                  |
| bench_mp_pool                    | 50.9 ms                                                | 61.8 ms: 1.21x slower                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 610 ms: 1.22x slower                                                   |
| genshi_xml                       | 34.4 ms                                                | 42.7 ms: 1.24x slower                                                  |
| async_tree_eager_io              | 513 ms                                                 | 667 ms: 1.30x slower                                                   |
| async_tree_eager_io_tg           | 477 ms                                                 | 712 ms: 1.49x slower                                                   |
| create_gc_cycles                 | 803 us                                                 | 1.31 ms: 1.64x slower                                                  |
| unpack_sequence                  | 36.1 ns                                                | 76.0 ns: 2.11x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (7): asyncio_tcp, tornado_http, async_tree_cpu_io_mixed, pidigits, dulwich_log, regex_dna, logging_silent
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20241016-3.14.0a1+-760872e-JIT/bm-20241016-darwin-arm64-python-760872efecb95017db8e-3.14.0a1+-760872e.json: sphinx

# HPT report

- Reliability score: 99.84% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 6.75x