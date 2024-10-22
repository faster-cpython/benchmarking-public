# Results vs. 3.13.0

- fork: python
- ref: 5e9e50612eb27aef8f74
- machine: darwin-arm64
- commit hash: 5e9e506
- commit date: 2024-10-04
- overall geometric mean: 1.03x faster
- HPT reliability: 99.80%
- HPT 99th percentile: 1.00x faster
- Memory change: 6.58x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 178 ms                                                 | 181 ms: 1.02x slower                                                  |
| docutils       | 1.44 sec                                               | 1.57 sec: 1.09x slower                                                |
| html5lib       | 36.6 ms                                                | 33.9 ms: 1.08x faster                                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| coroutines                       | 19.8 ms                                                | 16.3 ms: 1.21x faster                                                 |
| async_tree_memoization_tg        | 291 ms                                                 | 246 ms: 1.18x faster                                                  |
| async_tree_eager_tg              | 48.4 ms                                                | 41.4 ms: 1.17x faster                                                 |
| async_tree_eager                 | 70.5 ms                                                | 63.0 ms: 1.12x faster                                                 |
| async_tree_eager_memoization     | 169 ms                                                 | 153 ms: 1.11x faster                                                  |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 129 ms: 1.08x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 198 ms: 1.07x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 335 ms: 1.04x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 362 ms: 1.04x faster                                                  |
| async_generators                 | 294 ms                                                 | 290 ms: 1.01x faster                                                  |
| asyncio_websockets               | 241 ms                                                 | 242 ms: 1.00x slower                                                  |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.29 sec: 1.02x slower                                                |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 460 ms: 1.03x slower                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 541 ms: 1.08x slower                                                  |
| async_tree_io                    | 507 ms                                                 | 581 ms: 1.15x slower                                                  |
| async_tree_eager_io              | 513 ms                                                 | 683 ms: 1.33x slower                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 703 ms: 1.47x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (4): asyncio_tcp, async_tree_memoization, async_tree_none_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 56.2 ms                                                | 46.4 ms: 1.21x faster                                                 |
| nbody          | 73.9 ms                                                | 63.6 ms: 1.16x faster                                                 |
| pidigits       | 284 ms                                                 | 283 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.12x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 78.5 ms                                                | 76.1 ms: 1.03x faster                                                 |
| regex_effbot   | 2.63 ms                                                | 2.61 ms: 1.01x faster                                                 |
| regex_v8       | 16.9 ms                                                | 16.8 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle_pure_python | 163 us                                                 | 131 us: 1.24x faster                                                  |
| tomli_loads          | 1.56 sec                                               | 1.25 sec: 1.24x faster                                                |
| pickle_pure_python   | 213 us                                                 | 177 us: 1.20x faster                                                  |
| xml_etree_process    | 40.9 ms                                                | 34.3 ms: 1.19x faster                                                 |
| xml_etree_generate   | 56.6 ms                                                | 49.4 ms: 1.15x faster                                                 |
| json_dumps           | 6.56 ms                                                | 6.10 ms: 1.08x faster                                                 |
| xml_etree_parse      | 109 ms                                                 | 104 ms: 1.05x faster                                                  |
| xml_etree_iterparse  | 74.2 ms                                                | 72.4 ms: 1.02x faster                                                 |
| json_loads           | 16.9 us                                                | 16.5 us: 1.02x faster                                                 |
| unpickle             | 9.15 us                                                | 9.03 us: 1.01x faster                                                 |
| pickle_dict          | 18.2 us                                                | 18.2 us: 1.00x slower                                                 |
| pickle_list          | 2.99 us                                                | 3.01 us: 1.01x slower                                                 |
| unpickle_list        | 2.93 us                                                | 2.97 us: 1.01x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                          |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 13.7 ms                                                | 14.8 ms: 1.08x slower                                                 |
| python_startup         | 17.0 ms                                                | 19.1 ms: 1.12x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 7.68 ms                                                | 6.41 ms: 1.20x faster                                                 |
| genshi_text     | 16.9 ms                                                | 16.3 ms: 1.03x faster                                                 |
| django_template | 22.2 ms                                                | 23.0 ms: 1.03x slower                                                 |
| genshi_xml      | 34.4 ms                                                | 42.4 ms: 1.23x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo                    | 27.2 us                                                | 16.7 us: 1.63x faster                                                 |
| deepcopy                         | 232 us                                                 | 155 us: 1.50x faster                                                  |
| deepcopy_reduce                  | 2.06 us                                                | 1.51 us: 1.36x faster                                                 |
| generators                       | 31.5 ms                                                | 25.2 ms: 1.25x faster                                                 |
| unpickle_pure_python             | 163 us                                                 | 131 us: 1.24x faster                                                  |
| tomli_loads                      | 1.56 sec                                               | 1.25 sec: 1.24x faster                                                |
| logging_silent                   | 69.9 ns                                                | 56.4 ns: 1.24x faster                                                 |
| scimark_sor                      | 106 ms                                                 | 85.8 ms: 1.23x faster                                                 |
| float                            | 56.2 ms                                                | 46.4 ms: 1.21x faster                                                 |
| coroutines                       | 19.8 ms                                                | 16.3 ms: 1.21x faster                                                 |
| pickle_pure_python               | 213 us                                                 | 177 us: 1.20x faster                                                  |
| mako                             | 7.68 ms                                                | 6.41 ms: 1.20x faster                                                 |
| scimark_lu                       | 76.5 ms                                                | 64.1 ms: 1.19x faster                                                 |
| xml_etree_process                | 40.9 ms                                                | 34.3 ms: 1.19x faster                                                 |
| async_tree_memoization_tg        | 291 ms                                                 | 246 ms: 1.18x faster                                                  |
| async_tree_eager_tg              | 48.4 ms                                                | 41.4 ms: 1.17x faster                                                 |
| nbody                            | 73.9 ms                                                | 63.6 ms: 1.16x faster                                                 |
| logging_simple                   | 3.57 us                                                | 3.10 us: 1.15x faster                                                 |
| xml_etree_generate               | 56.6 ms                                                | 49.4 ms: 1.15x faster                                                 |
| logging_format                   | 3.85 us                                                | 3.41 us: 1.13x faster                                                 |
| spectral_norm                    | 77.3 ms                                                | 68.7 ms: 1.12x faster                                                 |
| scimark_monte_carlo              | 50.4 ms                                                | 45.1 ms: 1.12x faster                                                 |
| async_tree_eager                 | 70.5 ms                                                | 63.0 ms: 1.12x faster                                                 |
| thrift                           | 466 us                                                 | 420 us: 1.11x faster                                                  |
| async_tree_eager_memoization     | 169 ms                                                 | 153 ms: 1.11x faster                                                  |
| deltablue                        | 2.68 ms                                                | 2.42 ms: 1.11x faster                                                 |
| nqueens                          | 62.9 ms                                                | 57.1 ms: 1.10x faster                                                 |
| pyflate                          | 351 ms                                                 | 323 ms: 1.09x faster                                                  |
| scimark_fft                      | 201 ms                                                 | 185 ms: 1.09x faster                                                  |
| html5lib                         | 36.6 ms                                                | 33.9 ms: 1.08x faster                                                 |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 129 ms: 1.08x faster                                                  |
| json_dumps                       | 6.56 ms                                                | 6.10 ms: 1.08x faster                                                 |
| pprint_pformat                   | 1.08 sec                                               | 1.01 sec: 1.07x faster                                                |
| telco                            | 4.80 ms                                                | 4.50 ms: 1.07x faster                                                 |
| async_tree_none                  | 212 ms                                                 | 198 ms: 1.07x faster                                                  |
| typing_runtime_protocols         | 101 us                                                 | 95.0 us: 1.06x faster                                                 |
| bench_thread_pool                | 506 us                                                 | 480 us: 1.05x faster                                                  |
| coverage                         | 46.1 ms                                                | 43.9 ms: 1.05x faster                                                 |
| pprint_safe_repr                 | 531 ms                                                 | 506 ms: 1.05x faster                                                  |
| fannkuch                         | 282 ms                                                 | 269 ms: 1.05x faster                                                  |
| xml_etree_parse                  | 109 ms                                                 | 104 ms: 1.05x faster                                                  |
| bpe_tokeniser                    | 3.24 sec                                               | 3.10 sec: 1.05x faster                                                |
| go                               | 115 ms                                                 | 110 ms: 1.04x faster                                                  |
| crypto_pyaes                     | 54.0 ms                                                | 51.9 ms: 1.04x faster                                                 |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 335 ms: 1.04x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 362 ms: 1.04x faster                                                  |
| pycparser                        | 706 ms                                                 | 682 ms: 1.03x faster                                                  |
| genshi_text                      | 16.9 ms                                                | 16.3 ms: 1.03x faster                                                 |
| regex_compile                    | 78.5 ms                                                | 76.1 ms: 1.03x faster                                                 |
| xml_etree_iterparse              | 74.2 ms                                                | 72.4 ms: 1.02x faster                                                 |
| json_loads                       | 16.9 us                                                | 16.5 us: 1.02x faster                                                 |
| pathlib                          | 22.8 ms                                                | 22.3 ms: 1.02x faster                                                 |
| json                             | 2.94 ms                                                | 2.89 ms: 1.02x faster                                                 |
| async_generators                 | 294 ms                                                 | 290 ms: 1.01x faster                                                  |
| unpickle                         | 9.15 us                                                | 9.03 us: 1.01x faster                                                 |
| sqlglot_normalize                | 189 ms                                                 | 187 ms: 1.01x faster                                                  |
| regex_effbot                     | 2.63 ms                                                | 2.61 ms: 1.01x faster                                                 |
| regex_v8                         | 16.9 ms                                                | 16.8 ms: 1.01x faster                                                 |
| sqlite_synth                     | 1.54 us                                                | 1.53 us: 1.01x faster                                                 |
| chaos                            | 41.3 ms                                                | 41.0 ms: 1.00x faster                                                 |
| richards_super                   | 39.1 ms                                                | 39.0 ms: 1.00x faster                                                 |
| sympy_expand                     | 246 ms                                                 | 246 ms: 1.00x faster                                                  |
| pidigits                         | 284 ms                                                 | 283 ms: 1.00x faster                                                  |
| asyncio_websockets               | 241 ms                                                 | 242 ms: 1.00x slower                                                  |
| pickle_dict                      | 18.2 us                                                | 18.2 us: 1.00x slower                                                 |
| richards                         | 35.4 ms                                                | 35.6 ms: 1.00x slower                                                 |
| pickle_list                      | 2.99 us                                                | 3.01 us: 1.01x slower                                                 |
| dulwich_log                      | 28.7 ms                                                | 29.0 ms: 1.01x slower                                                 |
| unpickle_list                    | 2.93 us                                                | 2.97 us: 1.01x slower                                                 |
| 2to3                             | 178 ms                                                 | 181 ms: 1.02x slower                                                  |
| hexiom                           | 4.85 ms                                                | 4.96 ms: 1.02x slower                                                 |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.29 sec: 1.02x slower                                                |
| sqlglot_transpile                | 1.02 ms                                                | 1.05 ms: 1.03x slower                                                 |
| sympy_str                        | 145 ms                                                 | 150 ms: 1.03x slower                                                  |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 460 ms: 1.03x slower                                                  |
| meteor_contest                   | 73.8 ms                                                | 76.3 ms: 1.03x slower                                                 |
| django_template                  | 22.2 ms                                                | 23.0 ms: 1.03x slower                                                 |
| sympy_sum                        | 75.6 ms                                                | 78.3 ms: 1.04x slower                                                 |
| comprehensions                   | 12.2 us                                                | 12.8 us: 1.05x slower                                                 |
| raytrace                         | 182 ms                                                 | 191 ms: 1.05x slower                                                  |
| sqlglot_optimize                 | 34.9 ms                                                | 37.5 ms: 1.07x slower                                                 |
| async_tree_io_tg                 | 500 ms                                                 | 541 ms: 1.08x slower                                                  |
| python_startup_no_site           | 13.7 ms                                                | 14.8 ms: 1.08x slower                                                 |
| docutils                         | 1.44 sec                                               | 1.57 sec: 1.09x slower                                                |
| sympy_integrate                  | 11.3 ms                                                | 12.5 ms: 1.10x slower                                                 |
| python_startup                   | 17.0 ms                                                | 19.1 ms: 1.12x slower                                                 |
| async_tree_io                    | 507 ms                                                 | 581 ms: 1.15x slower                                                  |
| gc_traversal                     | 2.48 ms                                                | 2.91 ms: 1.17x slower                                                 |
| pylint                           | 181 ms                                                 | 212 ms: 1.17x slower                                                  |
| bench_mp_pool                    | 50.9 ms                                                | 62.2 ms: 1.22x slower                                                 |
| genshi_xml                       | 34.4 ms                                                | 42.4 ms: 1.23x slower                                                 |
| async_tree_eager_io              | 513 ms                                                 | 683 ms: 1.33x slower                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 703 ms: 1.47x slower                                                  |
| create_gc_cycles                 | 803 us                                                 | 1.29 ms: 1.60x slower                                                 |
| unpack_sequence                  | 36.1 ns                                                | 75.7 ns: 2.10x slower                                                 |
| Geometric mean                   | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (10): asyncio_tcp, async_tree_memoization, async_tree_none_tg, async_tree_cpu_io_mixed, tornado_http, sqlglot_parse, pickle, scimark_sparse_mat_mult, regex_dna, mdp
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20241004-3.14.0a0-5e9e506-JIT/bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506.json: sphinx

# HPT report

- Reliability score: 99.80% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 6.58x