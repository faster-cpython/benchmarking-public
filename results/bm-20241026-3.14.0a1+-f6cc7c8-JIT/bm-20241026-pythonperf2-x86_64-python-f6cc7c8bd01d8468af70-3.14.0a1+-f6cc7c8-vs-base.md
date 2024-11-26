# Results vs. base

- fork: python
- ref: f6cc7c8bd01d8468af70
- machine: linux-x86_64
- commit hash: f6cc7c8
- commit date: 2024-10-26
- overall geometric mean: 1.030x slower
- HPT reliability: 98.93%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20241026-3.14.0a1+-f6cc7c8/bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json | results/bm-20241026-3.14.0a1+-f6cc7c8-JIT/bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 283 ms                                                                                                                  | 317 ms: 1.12x slower                                                                                                        |
| docutils       | 2.92 sec                                                                                                                | 3.20 sec: 1.10x slower                                                                                                      |
| html5lib       | 72.3 ms                                                                                                                 | 70.7 ms: 1.02x faster                                                                                                       |
| sphinx         | 1.13 sec                                                                                                                | 1.27 sec: 1.13x slower                                                                                                      |
| tornado_http   | 117 ms                                                                                                                  | 122 ms: 1.04x slower                                                                                                        |
| Geometric mean | (ref)                                                                                                                   | 1.07x slower                                                                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | results/bm-20241026-3.14.0a1+-f6cc7c8/bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json | results/bm-20241026-3.14.0a1+-f6cc7c8-JIT/bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json |
|---------------------------|:-----------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------:|
| async_tree_memoization    | 417 ms                                                                                                                  | 402 ms: 1.04x faster                                                                                                        |
| async_tree_io_tg          | 863 ms                                                                                                                  | 836 ms: 1.03x faster                                                                                                        |
| coroutines                | 21.0 ms                                                                                                                 | 21.3 ms: 1.02x slower                                                                                                       |
| async_tree_cpu_io_mixed   | 560 ms                                                                                                                  | 573 ms: 1.02x slower                                                                                                        |
| async_tree_memoization_tg | 373 ms                                                                                                                  | 382 ms: 1.03x slower                                                                                                        |
| async_tree_none_tg        | 322 ms                                                                                                                  | 333 ms: 1.03x slower                                                                                                        |
| async_generators          | 365 ms                                                                                                                  | 379 ms: 1.04x slower                                                                                                        |
| Geometric mean            | (ref)                                                                                                                   | 1.01x slower                                                                                                                |

Benchmark hidden because not significant (4): async_tree_cpu_io_mixed_tg, async_tree_io, asyncio_websockets, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20241026-3.14.0a1+-f6cc7c8/bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json | results/bm-20241026-3.14.0a1+-f6cc7c8-JIT/bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 91.1 ms                                                                                                                 | 83.8 ms: 1.09x faster                                                                                                       |
| float          | 81.4 ms                                                                                                                 | 80.0 ms: 1.02x faster                                                                                                       |
| pidigits       | 253 ms                                                                                                                  | 251 ms: 1.01x faster                                                                                                        |
| Geometric mean | (ref)                                                                                                                   | 1.04x faster                                                                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20241026-3.14.0a1+-f6cc7c8/bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json | results/bm-20241026-3.14.0a1+-f6cc7c8-JIT/bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 246 ms                                                                                                                  | 240 ms: 1.02x faster                                                                                                        |
| regex_v8       | 25.4 ms                                                                                                                 | 25.1 ms: 1.01x faster                                                                                                       |
| regex_effbot   | 3.52 ms                                                                                                                 | 3.60 ms: 1.02x slower                                                                                                       |
| regex_compile  | 139 ms                                                                                                                  | 147 ms: 1.06x slower                                                                                                        |
| Geometric mean | (ref)                                                                                                                   | 1.01x slower                                                                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20241026-3.14.0a1+-f6cc7c8/bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json | results/bm-20241026-3.14.0a1+-f6cc7c8-JIT/bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json |
|----------------------|:-----------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 2.47 sec                                                                                                                | 2.07 sec: 1.19x faster                                                                                                      |
| xml_etree_generate   | 85.0 ms                                                                                                                 | 80.9 ms: 1.05x faster                                                                                                       |
| json_dumps           | 11.4 ms                                                                                                                 | 11.0 ms: 1.03x faster                                                                                                       |
| xml_etree_process    | 59.3 ms                                                                                                                 | 57.7 ms: 1.03x faster                                                                                                       |
| xml_etree_parse      | 146 ms                                                                                                                  | 144 ms: 1.01x faster                                                                                                        |
| xml_etree_iterparse  | 101 ms                                                                                                                  | 100 ms: 1.01x faster                                                                                                        |
| unpickle_pure_python | 220 us                                                                                                                  | 221 us: 1.01x slower                                                                                                        |
| json_loads           | 24.5 us                                                                                                                 | 25.1 us: 1.02x slower                                                                                                       |
| pickle_pure_python   | 325 us                                                                                                                  | 336 us: 1.04x slower                                                                                                        |
| Geometric mean       | (ref)                                                                                                                   | 1.03x faster                                                                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark      | results/bm-20241026-3.14.0a1+-f6cc7c8/bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json | results/bm-20241026-3.14.0a1+-f6cc7c8-JIT/bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------:|
| python_startup | 15.7 ms                                                                                                                 | 15.8 ms: 1.01x slower                                                                                                       |
| Geometric mean | (ref)                                                                                                                   | 1.00x slower                                                                                                                |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20241026-3.14.0a1+-f6cc7c8/bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json | results/bm-20241026-3.14.0a1+-f6cc7c8-JIT/bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json |
|-----------------|:-----------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------:|
| mako            | 10.7 ms                                                                                                                 | 9.49 ms: 1.13x faster                                                                                                       |
| django_template | 40.2 ms                                                                                                                 | 44.4 ms: 1.11x slower                                                                                                       |
| genshi_text     | 24.7 ms                                                                                                                 | 30.2 ms: 1.22x slower                                                                                                       |
| genshi_xml      | 55.2 ms                                                                                                                 | 67.9 ms: 1.23x slower                                                                                                       |
| Geometric mean  | (ref)                                                                                                                   | 1.10x slower                                                                                                                |

All benchmarks:
===============

| Benchmark                 | results/bm-20241026-3.14.0a1+-f6cc7c8/bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json | results/bm-20241026-3.14.0a1+-f6cc7c8-JIT/bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json |
|---------------------------|:-----------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------:|
| tomli_loads               | 2.47 sec                                                                                                                | 2.07 sec: 1.19x faster                                                                                                      |
| richards                  | 49.5 ms                                                                                                                 | 43.7 ms: 1.13x faster                                                                                                       |
| mako                      | 10.7 ms                                                                                                                 | 9.49 ms: 1.13x faster                                                                                                       |
| richards_super            | 55.4 ms                                                                                                                 | 49.3 ms: 1.12x faster                                                                                                       |
| scimark_sor               | 117 ms                                                                                                                  | 105 ms: 1.11x faster                                                                                                        |
| nbody                     | 91.1 ms                                                                                                                 | 83.8 ms: 1.09x faster                                                                                                       |
| pyflate                   | 479 ms                                                                                                                  | 450 ms: 1.06x faster                                                                                                        |
| spectral_norm             | 99.3 ms                                                                                                                 | 93.6 ms: 1.06x faster                                                                                                       |
| xml_etree_generate        | 85.0 ms                                                                                                                 | 80.9 ms: 1.05x faster                                                                                                       |
| logging_silent            | 98.2 ns                                                                                                                 | 94.2 ns: 1.04x faster                                                                                                       |
| create_gc_cycles          | 2.98 ms                                                                                                                 | 2.87 ms: 1.04x faster                                                                                                       |
| async_tree_memoization    | 417 ms                                                                                                                  | 402 ms: 1.04x faster                                                                                                        |
| deltablue                 | 3.42 ms                                                                                                                 | 3.30 ms: 1.04x faster                                                                                                       |
| dulwich_log               | 65.2 ms                                                                                                                 | 63.2 ms: 1.03x faster                                                                                                       |
| async_tree_io_tg          | 863 ms                                                                                                                  | 836 ms: 1.03x faster                                                                                                        |
| json_dumps                | 11.4 ms                                                                                                                 | 11.0 ms: 1.03x faster                                                                                                       |
| scimark_sparse_mat_mult   | 4.32 ms                                                                                                                 | 4.20 ms: 1.03x faster                                                                                                       |
| xml_etree_process         | 59.3 ms                                                                                                                 | 57.7 ms: 1.03x faster                                                                                                       |
| regex_dna                 | 246 ms                                                                                                                  | 240 ms: 1.02x faster                                                                                                        |
| html5lib                  | 72.3 ms                                                                                                                 | 70.7 ms: 1.02x faster                                                                                                       |
| telco                     | 7.94 ms                                                                                                                 | 7.81 ms: 1.02x faster                                                                                                       |
| float                     | 81.4 ms                                                                                                                 | 80.0 ms: 1.02x faster                                                                                                       |
| xml_etree_parse           | 146 ms                                                                                                                  | 144 ms: 1.01x faster                                                                                                        |
| scimark_fft               | 294 ms                                                                                                                  | 290 ms: 1.01x faster                                                                                                        |
| logging_format            | 7.21 us                                                                                                                 | 7.13 us: 1.01x faster                                                                                                       |
| xml_etree_iterparse       | 101 ms                                                                                                                  | 100 ms: 1.01x faster                                                                                                        |
| regex_v8                  | 25.4 ms                                                                                                                 | 25.1 ms: 1.01x faster                                                                                                       |
| pidigits                  | 253 ms                                                                                                                  | 251 ms: 1.01x faster                                                                                                        |
| python_startup            | 15.7 ms                                                                                                                 | 15.8 ms: 1.01x slower                                                                                                       |
| unpickle_pure_python      | 220 us                                                                                                                  | 221 us: 1.01x slower                                                                                                        |
| pathlib                   | 15.7 ms                                                                                                                 | 15.9 ms: 1.01x slower                                                                                                       |
| crypto_pyaes              | 72.3 ms                                                                                                                 | 73.0 ms: 1.01x slower                                                                                                       |
| coroutines                | 21.0 ms                                                                                                                 | 21.3 ms: 1.02x slower                                                                                                       |
| pprint_pformat            | 1.61 sec                                                                                                                | 1.63 sec: 1.02x slower                                                                                                      |
| regex_effbot              | 3.52 ms                                                                                                                 | 3.60 ms: 1.02x slower                                                                                                       |
| json_loads                | 24.5 us                                                                                                                 | 25.1 us: 1.02x slower                                                                                                       |
| async_tree_cpu_io_mixed   | 560 ms                                                                                                                  | 573 ms: 1.02x slower                                                                                                        |
| async_tree_memoization_tg | 373 ms                                                                                                                  | 382 ms: 1.03x slower                                                                                                        |
| async_tree_none_tg        | 322 ms                                                                                                                  | 333 ms: 1.03x slower                                                                                                        |
| coverage                  | 79.3 ms                                                                                                                 | 82.1 ms: 1.04x slower                                                                                                       |
| pickle_pure_python        | 325 us                                                                                                                  | 336 us: 1.04x slower                                                                                                        |
| gc_traversal              | 5.31 ms                                                                                                                 | 5.52 ms: 1.04x slower                                                                                                       |
| async_generators          | 365 ms                                                                                                                  | 379 ms: 1.04x slower                                                                                                        |
| mdp                       | 2.51 sec                                                                                                                | 2.62 sec: 1.04x slower                                                                                                      |
| tornado_http              | 117 ms                                                                                                                  | 122 ms: 1.04x slower                                                                                                        |
| pycparser                 | 1.24 sec                                                                                                                | 1.30 sec: 1.05x slower                                                                                                      |
| scimark_monte_carlo       | 66.5 ms                                                                                                                 | 69.7 ms: 1.05x slower                                                                                                       |
| typing_runtime_protocols  | 178 us                                                                                                                  | 187 us: 1.05x slower                                                                                                        |
| regex_compile             | 139 ms                                                                                                                  | 147 ms: 1.06x slower                                                                                                        |
| fannkuch                  | 352 ms                                                                                                                  | 372 ms: 1.06x slower                                                                                                        |
| bench_thread_pool         | 901 us                                                                                                                  | 954 us: 1.06x slower                                                                                                        |
| meteor_contest            | 126 ms                                                                                                                  | 134 ms: 1.06x slower                                                                                                        |
| sqlglot_parse             | 1.41 ms                                                                                                                 | 1.50 ms: 1.06x slower                                                                                                       |
| sympy_expand              | 502 ms                                                                                                                  | 535 ms: 1.07x slower                                                                                                        |
| deepcopy_memo             | 29.2 us                                                                                                                 | 31.2 us: 1.07x slower                                                                                                       |
| deepcopy_reduce           | 2.95 us                                                                                                                 | 3.14 us: 1.07x slower                                                                                                       |
| thrift                    | 855 us                                                                                                                  | 914 us: 1.07x slower                                                                                                        |
| chaos                     | 63.5 ms                                                                                                                 | 69.2 ms: 1.09x slower                                                                                                       |
| deepcopy                  | 291 us                                                                                                                  | 319 us: 1.10x slower                                                                                                        |
| docutils                  | 2.92 sec                                                                                                                | 3.20 sec: 1.10x slower                                                                                                      |
| comprehensions            | 17.6 us                                                                                                                 | 19.4 us: 1.10x slower                                                                                                       |
| sqlglot_transpile         | 1.79 ms                                                                                                                 | 1.97 ms: 1.10x slower                                                                                                       |
| django_template           | 40.2 ms                                                                                                                 | 44.4 ms: 1.11x slower                                                                                                       |
| sympy_str                 | 292 ms                                                                                                                  | 323 ms: 1.11x slower                                                                                                        |
| raytrace                  | 279 ms                                                                                                                  | 310 ms: 1.11x slower                                                                                                        |
| 2to3                      | 283 ms                                                                                                                  | 317 ms: 1.12x slower                                                                                                        |
| go                        | 136 ms                                                                                                                  | 153 ms: 1.12x slower                                                                                                        |
| hexiom                    | 6.40 ms                                                                                                                 | 7.18 ms: 1.12x slower                                                                                                       |
| sphinx                    | 1.13 sec                                                                                                                | 1.27 sec: 1.13x slower                                                                                                      |
| sqlglot_normalize         | 118 ms                                                                                                                  | 135 ms: 1.14x slower                                                                                                        |
| nqueens                   | 90.4 ms                                                                                                                 | 104 ms: 1.15x slower                                                                                                        |
| sympy_sum                 | 153 ms                                                                                                                  | 176 ms: 1.16x slower                                                                                                        |
| sympy_integrate           | 23.4 ms                                                                                                                 | 27.3 ms: 1.17x slower                                                                                                       |
| sqlglot_optimize          | 58.7 ms                                                                                                                 | 68.9 ms: 1.17x slower                                                                                                       |
| sqlalchemy_declarative    | 142 ms                                                                                                                  | 168 ms: 1.18x slower                                                                                                        |
| pylint                    | 349 ms                                                                                                                  | 423 ms: 1.21x slower                                                                                                        |
| genshi_text               | 24.7 ms                                                                                                                 | 30.2 ms: 1.22x slower                                                                                                       |
| genshi_xml                | 55.2 ms                                                                                                                 | 67.9 ms: 1.23x slower                                                                                                       |
| generators                | 29.2 ms                                                                                                                 | 38.8 ms: 1.33x slower                                                                                                       |
| Geometric mean            | (ref)                                                                                                                   | 1.03x slower                                                                                                                |

Benchmark hidden because not significant (12): async_tree_cpu_io_mixed_tg, json, logging_simple, scimark_lu, pprint_safe_repr, bpe_tokeniser, python_startup_no_site, sqlalchemy_imperative, async_tree_io, asyncio_websockets, async_tree_none, bench_mp_pool

- Geometric mean (including insignificant results): 1.030x slower
# HPT report

- Reliability score: 98.93% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.06x