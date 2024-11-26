# Results vs. 3.13.0

- fork: python
- ref: c695e37a3f95c225ee08
- machine: windows-amd64
- commit hash: c695e37
- commit date: 2024-11-13
- overall geometric mean: 1.004x slower
- HPT reliability: 95.06%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241113-pythonperf1-amd64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 245 ms: 1.11x slower                                                        |
| docutils       | 1.57 sec                                                    | 1.89 sec: 1.20x slower                                                      |
| sphinx         | 633 ms                                                      | 763 ms: 1.21x slower                                                        |
| Geometric mean | (ref)                                                       | 1.12x slower                                                                |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241113-pythonperf1-amd64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 259 ms: 1.11x faster                                                        |
| async_tree_none            | 226 ms                                                      | 209 ms: 1.08x faster                                                        |
| async_tree_memoization     | 276 ms                                                      | 262 ms: 1.05x faster                                                        |
| asyncio_websockets         | 318 ms                                                      | 311 ms: 1.02x faster                                                        |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 391 ms: 1.02x slower                                                        |
| async_tree_none_tg         | 209 ms                                                      | 219 ms: 1.05x slower                                                        |
| coroutines                 | 12.8 ms                                                     | 13.4 ms: 1.05x slower                                                       |
| async_tree_io              | 521 ms                                                      | 553 ms: 1.06x slower                                                        |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 401 ms: 1.07x slower                                                        |
| async_generators           | 223 ms                                                      | 267 ms: 1.20x slower                                                        |
| async_tree_io_tg           | 518 ms                                                      | 630 ms: 1.22x slower                                                        |
| Geometric mean             | (ref)                                                       | 1.03x slower                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241113-pythonperf1-amd64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 68.4 ms                                                     | 52.8 ms: 1.30x faster                                                       |
| float          | 49.9 ms                                                     | 47.4 ms: 1.05x faster                                                       |
| pidigits       | 148 ms                                                      | 147 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                       | 1.11x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241113-pythonperf1-amd64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 14.6 ms: 1.46x faster                                                       |
| regex_effbot   | 1.58 ms                                                     | 1.54 ms: 1.02x faster                                                       |
| regex_dna      | 115 ms                                                      | 116 ms: 1.01x slower                                                        |
| regex_compile  | 80.5 ms                                                     | 90.2 ms: 1.12x slower                                                       |
| Geometric mean | (ref)                                                       | 1.07x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241113-pythonperf1-amd64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 1.39 sec                                                    | 1.27 sec: 1.10x faster                                                      |
| xml_etree_generate   | 54.0 ms                                                     | 51.0 ms: 1.06x faster                                                       |
| json_loads           | 15.1 us                                                     | 14.3 us: 1.06x faster                                                       |
| xml_etree_process    | 37.0 ms                                                     | 36.3 ms: 1.02x faster                                                       |
| xml_etree_parse      | 93.6 ms                                                     | 92.7 ms: 1.01x faster                                                       |
| xml_etree_iterparse  | 61.8 ms                                                     | 62.4 ms: 1.01x slower                                                       |
| json_dumps           | 5.92 ms                                                     | 6.38 ms: 1.08x slower                                                       |
| pickle_pure_python   | 190 us                                                      | 208 us: 1.10x slower                                                        |
| unpickle_pure_python | 133 us                                                      | 147 us: 1.10x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.00x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241113-pythonperf1-amd64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 25.4 ms                                                     | 23.3 ms: 1.09x faster                                                       |
| python_startup_no_site | 18.1 ms                                                     | 17.7 ms: 1.03x faster                                                       |
| Geometric mean         | (ref)                                                       | 1.06x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241113-pythonperf1-amd64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 6.35 ms                                                     | 5.18 ms: 1.23x faster                                                       |
| django_template | 22.4 ms                                                     | 26.7 ms: 1.19x slower                                                       |
| genshi_text     | 15.6 ms                                                     | 19.2 ms: 1.23x slower                                                       |
| genshi_xml      | 35.5 ms                                                     | 46.0 ms: 1.30x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.12x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241113-pythonperf1-amd64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.80 ms                                                     | 527 us: 16.69x faster                                                       |
| regex_v8                   | 21.4 ms                                                     | 14.6 ms: 1.46x faster                                                       |
| deepcopy_memo              | 23.3 us                                                     | 16.2 us: 1.44x faster                                                       |
| nbody                      | 68.4 ms                                                     | 52.8 ms: 1.30x faster                                                       |
| mako                       | 6.35 ms                                                     | 5.18 ms: 1.23x faster                                                       |
| deepcopy                   | 226 us                                                      | 186 us: 1.22x faster                                                        |
| scimark_sor                | 76.2 ms                                                     | 64.1 ms: 1.19x faster                                                       |
| crypto_pyaes               | 45.4 ms                                                     | 39.6 ms: 1.15x faster                                                       |
| spectral_norm              | 62.8 ms                                                     | 55.4 ms: 1.13x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 259 ms: 1.11x faster                                                        |
| scimark_fft                | 172 ms                                                      | 155 ms: 1.11x faster                                                        |
| scimark_sparse_mat_mult    | 2.46 ms                                                     | 2.22 ms: 1.11x faster                                                       |
| scimark_monte_carlo        | 40.8 ms                                                     | 36.9 ms: 1.11x faster                                                       |
| deepcopy_reduce            | 2.06 us                                                     | 1.87 us: 1.10x faster                                                       |
| tomli_loads                | 1.39 sec                                                    | 1.27 sec: 1.10x faster                                                      |
| pprint_safe_repr           | 494 ms                                                      | 452 ms: 1.09x faster                                                        |
| python_startup             | 25.4 ms                                                     | 23.3 ms: 1.09x faster                                                       |
| json                       | 3.19 ms                                                     | 2.94 ms: 1.08x faster                                                       |
| telco                      | 4.79 ms                                                     | 4.43 ms: 1.08x faster                                                       |
| async_tree_none            | 226 ms                                                      | 209 ms: 1.08x faster                                                        |
| pprint_pformat             | 999 ms                                                      | 924 ms: 1.08x faster                                                        |
| pathlib                    | 80.9 ms                                                     | 74.9 ms: 1.08x faster                                                       |
| bpe_tokeniser              | 2.91 sec                                                    | 2.69 sec: 1.08x faster                                                      |
| xml_etree_generate         | 54.0 ms                                                     | 51.0 ms: 1.06x faster                                                       |
| json_loads                 | 15.1 us                                                     | 14.3 us: 1.06x faster                                                       |
| float                      | 49.9 ms                                                     | 47.4 ms: 1.05x faster                                                       |
| async_tree_memoization     | 276 ms                                                      | 262 ms: 1.05x faster                                                        |
| connected_components       | 332 ms                                                      | 316 ms: 1.05x faster                                                        |
| fannkuch                   | 253 ms                                                      | 243 ms: 1.04x faster                                                        |
| shortest_path              | 362 ms                                                      | 349 ms: 1.04x faster                                                        |
| gc_traversal               | 1.97 ms                                                     | 1.91 ms: 1.03x faster                                                       |
| python_startup_no_site     | 18.1 ms                                                     | 17.7 ms: 1.03x faster                                                       |
| dulwich_log                | 40.8 ms                                                     | 39.8 ms: 1.02x faster                                                       |
| asyncio_websockets         | 318 ms                                                      | 311 ms: 1.02x faster                                                        |
| regex_effbot               | 1.58 ms                                                     | 1.54 ms: 1.02x faster                                                       |
| xml_etree_process          | 37.0 ms                                                     | 36.3 ms: 1.02x faster                                                       |
| xml_etree_parse            | 93.6 ms                                                     | 92.7 ms: 1.01x faster                                                       |
| pidigits                   | 148 ms                                                      | 147 ms: 1.01x faster                                                        |
| meteor_contest             | 73.5 ms                                                     | 72.9 ms: 1.01x faster                                                       |
| regex_dna                  | 115 ms                                                      | 116 ms: 1.01x slower                                                        |
| xml_etree_iterparse        | 61.8 ms                                                     | 62.4 ms: 1.01x slower                                                       |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 391 ms: 1.02x slower                                                        |
| scimark_lu                 | 53.0 ms                                                     | 54.2 ms: 1.02x slower                                                       |
| logging_simple             | 5.96 us                                                     | 6.10 us: 1.02x slower                                                       |
| go                         | 87.0 ms                                                     | 91.0 ms: 1.05x slower                                                       |
| logging_format             | 6.26 us                                                     | 6.56 us: 1.05x slower                                                       |
| async_tree_none_tg         | 209 ms                                                      | 219 ms: 1.05x slower                                                        |
| coverage                   | 45.6 ms                                                     | 47.8 ms: 1.05x slower                                                       |
| pycparser                  | 683 ms                                                      | 718 ms: 1.05x slower                                                        |
| coroutines                 | 12.8 ms                                                     | 13.4 ms: 1.05x slower                                                       |
| async_tree_io              | 521 ms                                                      | 553 ms: 1.06x slower                                                        |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 401 ms: 1.07x slower                                                        |
| chaos                      | 38.5 ms                                                     | 41.4 ms: 1.07x slower                                                       |
| json_dumps                 | 5.92 ms                                                     | 6.38 ms: 1.08x slower                                                       |
| create_gc_cycles           | 1.26 ms                                                     | 1.37 ms: 1.09x slower                                                       |
| pickle_pure_python         | 190 us                                                      | 208 us: 1.10x slower                                                        |
| unpickle_pure_python       | 133 us                                                      | 147 us: 1.10x slower                                                        |
| sympy_expand               | 291 ms                                                      | 322 ms: 1.11x slower                                                        |
| pyflate                    | 283 ms                                                      | 313 ms: 1.11x slower                                                        |
| 2to3                       | 221 ms                                                      | 245 ms: 1.11x slower                                                        |
| typing_runtime_protocols   | 105 us                                                      | 117 us: 1.11x slower                                                        |
| regex_compile              | 80.5 ms                                                     | 90.2 ms: 1.12x slower                                                       |
| sympy_str                  | 169 ms                                                      | 190 ms: 1.12x slower                                                        |
| mdp                        | 1.39 sec                                                    | 1.59 sec: 1.14x slower                                                      |
| nqueens                    | 56.7 ms                                                     | 65.7 ms: 1.16x slower                                                       |
| comprehensions             | 10.3 us                                                     | 11.9 us: 1.16x slower                                                       |
| sqlglot_parse              | 771 us                                                      | 899 us: 1.17x slower                                                        |
| generators                 | 19.5 ms                                                     | 22.8 ms: 1.17x slower                                                       |
| sympy_sum                  | 86.9 ms                                                     | 102 ms: 1.17x slower                                                        |
| django_template            | 22.4 ms                                                     | 26.7 ms: 1.19x slower                                                       |
| async_generators           | 223 ms                                                      | 267 ms: 1.20x slower                                                        |
| docutils                   | 1.57 sec                                                    | 1.89 sec: 1.20x slower                                                      |
| sqlglot_normalize          | 175 ms                                                      | 210 ms: 1.20x slower                                                        |
| sphinx                     | 633 ms                                                      | 763 ms: 1.21x slower                                                        |
| async_tree_io_tg           | 518 ms                                                      | 630 ms: 1.22x slower                                                        |
| genshi_text                | 15.6 ms                                                     | 19.2 ms: 1.23x slower                                                       |
| deltablue                  | 1.92 ms                                                     | 2.36 ms: 1.23x slower                                                       |
| sqlglot_transpile          | 956 us                                                      | 1.18 ms: 1.24x slower                                                       |
| sympy_integrate            | 12.5 ms                                                     | 15.6 ms: 1.25x slower                                                       |
| richards_super             | 30.9 ms                                                     | 39.4 ms: 1.28x slower                                                       |
| richards                   | 27.3 ms                                                     | 35.2 ms: 1.29x slower                                                       |
| genshi_xml                 | 35.5 ms                                                     | 46.0 ms: 1.30x slower                                                       |
| sqlglot_optimize           | 32.9 ms                                                     | 42.9 ms: 1.30x slower                                                       |
| pylint                     | 211 ms                                                      | 277 ms: 1.31x slower                                                        |
| hexiom                     | 3.89 ms                                                     | 5.19 ms: 1.33x slower                                                       |
| k_core                     | 1.74 sec                                                    | 2.42 sec: 1.39x slower                                                      |
| raytrace                   | 160 ms                                                      | 225 ms: 1.40x slower                                                        |
| Geometric mean             | (ref)                                                       | 1.00x slower                                                                |

Benchmark hidden because not significant (4): bench_thread_pool, html5lib, logging_silent, bench_mp_pool
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of results/bm-20241113-3.14.0a1+-c695e37-JIT/bm-20241113-pythonperf1-amd64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37.json: sqlite_synth

- Geometric mean (including insignificant results): 1.004x slower
# HPT report

- Reliability score: 95.06% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown