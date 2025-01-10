# Results vs. base

- fork: Fidget-Spinner
- ref: tail_call
- machine: windows-amd64
- commit hash: f1d3190
- commit date: 2025-01-07
- overall geometric mean: 1.108x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-pythonperf1-amd64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 239 ms                                                                      | 225 ms: 1.06x faster                                                       |
| docutils       | 1.79 sec                                                                    | 1.71 sec: 1.05x faster                                                     |
| html5lib       | 39.8 ms                                                                     | 36.6 ms: 1.09x faster                                                      |
| sphinx         | 706 ms                                                                      | 666 ms: 1.06x faster                                                       |
| Geometric mean | (ref)                                                                       | 1.07x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-pythonperf1-amd64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| coroutines                 | 14.6 ms                                                                     | 12.3 ms: 1.19x faster                                                      |
| async_tree_io              | 401 ms                                                                      | 363 ms: 1.11x faster                                                       |
| async_tree_none            | 177 ms                                                                      | 161 ms: 1.10x faster                                                       |
| async_generators           | 254 ms                                                                      | 233 ms: 1.09x faster                                                       |
| async_tree_none_tg         | 166 ms                                                                      | 154 ms: 1.08x faster                                                       |
| async_tree_io_tg           | 391 ms                                                                      | 364 ms: 1.07x faster                                                       |
| async_tree_memoization     | 218 ms                                                                      | 203 ms: 1.07x faster                                                       |
| async_tree_cpu_io_mixed_tg | 373 ms                                                                      | 365 ms: 1.02x faster                                                       |
| async_tree_cpu_io_mixed    | 373 ms                                                                      | 369 ms: 1.01x faster                                                       |
| Geometric mean             | (ref)                                                                       | 1.07x faster                                                               |

Benchmark hidden because not significant (2): async_tree_memoization_tg, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-pythonperf1-amd64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 68.8 ms                                                                     | 55.8 ms: 1.23x faster                                                      |
| float          | 55.1 ms                                                                     | 45.8 ms: 1.20x faster                                                      |
| Geometric mean | (ref)                                                                       | 1.14x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-pythonperf1-amd64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 91.0 ms                                                                     | 77.2 ms: 1.18x faster                                                      |
| regex_dna      | 142 ms                                                                      | 139 ms: 1.02x faster                                                       |
| regex_effbot   | 1.98 ms                                                                     | 1.99 ms: 1.00x slower                                                      |
| Geometric mean | (ref)                                                                       | 1.08x faster                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-pythonperf1-amd64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 159 us                                                                      | 126 us: 1.26x faster                                                       |
| tomli_loads          | 1.40 sec                                                                    | 1.15 sec: 1.22x faster                                                     |
| pickle_pure_python   | 228 us                                                                      | 189 us: 1.20x faster                                                       |
| xml_etree_process    | 47.3 ms                                                                     | 40.9 ms: 1.16x faster                                                      |
| xml_etree_generate   | 67.6 ms                                                                     | 61.4 ms: 1.10x faster                                                      |
| xml_etree_iterparse  | 71.0 ms                                                                     | 65.6 ms: 1.08x faster                                                      |
| json_dumps           | 7.79 ms                                                                     | 7.33 ms: 1.06x faster                                                      |
| xml_etree_parse      | 102 ms                                                                      | 97.9 ms: 1.04x faster                                                      |
| Geometric mean       | (ref)                                                                       | 1.12x faster                                                               |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-pythonperf1-amd64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|-----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 8.55 ms                                                                     | 7.19 ms: 1.19x faster                                                      |
| genshi_text     | 16.2 ms                                                                     | 13.8 ms: 1.18x faster                                                      |
| genshi_xml      | 34.1 ms                                                                     | 30.5 ms: 1.12x faster                                                      |
| django_template | 25.7 ms                                                                     | 23.3 ms: 1.10x faster                                                      |
| Geometric mean  | (ref)                                                                       | 1.15x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-pythonperf1-amd64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| scimark_sor                | 82.5 ms                                                                     | 60.3 ms: 1.37x faster                                                      |
| logging_silent             | 70.2 ns                                                                     | 51.3 ns: 1.37x faster                                                      |
| scimark_lu                 | 72.3 ms                                                                     | 53.4 ms: 1.35x faster                                                      |
| hexiom                     | 4.59 ms                                                                     | 3.48 ms: 1.32x faster                                                      |
| scimark_monte_carlo        | 45.7 ms                                                                     | 35.0 ms: 1.31x faster                                                      |
| deepcopy_memo              | 21.7 us                                                                     | 16.8 us: 1.30x faster                                                      |
| spectral_norm              | 73.1 ms                                                                     | 56.4 ms: 1.30x faster                                                      |
| go                         | 82.7 ms                                                                     | 64.8 ms: 1.28x faster                                                      |
| unpickle_pure_python       | 159 us                                                                      | 126 us: 1.26x faster                                                       |
| deltablue                  | 2.15 ms                                                                     | 1.71 ms: 1.25x faster                                                      |
| nbody                      | 68.8 ms                                                                     | 55.8 ms: 1.23x faster                                                      |
| richards                   | 31.1 ms                                                                     | 25.3 ms: 1.23x faster                                                      |
| fannkuch                   | 291 ms                                                                      | 237 ms: 1.23x faster                                                       |
| richards_super             | 35.3 ms                                                                     | 28.8 ms: 1.22x faster                                                      |
| tomli_loads                | 1.40 sec                                                                    | 1.15 sec: 1.22x faster                                                     |
| crypto_pyaes               | 57.7 ms                                                                     | 47.7 ms: 1.21x faster                                                      |
| pickle_pure_python         | 228 us                                                                      | 189 us: 1.20x faster                                                       |
| float                      | 55.1 ms                                                                     | 45.8 ms: 1.20x faster                                                      |
| sqlglot_parse              | 871 us                                                                      | 726 us: 1.20x faster                                                       |
| chaos                      | 45.2 ms                                                                     | 37.9 ms: 1.19x faster                                                      |
| coroutines                 | 14.6 ms                                                                     | 12.3 ms: 1.19x faster                                                      |
| pyflate                    | 332 ms                                                                      | 279 ms: 1.19x faster                                                       |
| mako                       | 8.55 ms                                                                     | 7.19 ms: 1.19x faster                                                      |
| comprehensions             | 12.9 us                                                                     | 10.8 us: 1.19x faster                                                      |
| scimark_fft                | 194 ms                                                                      | 164 ms: 1.18x faster                                                       |
| regex_compile              | 91.0 ms                                                                     | 77.2 ms: 1.18x faster                                                      |
| genshi_text                | 16.2 ms                                                                     | 13.8 ms: 1.18x faster                                                      |
| pprint_pformat             | 1.11 sec                                                                    | 952 ms: 1.17x faster                                                       |
| pprint_safe_repr           | 549 ms                                                                      | 472 ms: 1.16x faster                                                       |
| xml_etree_process          | 47.3 ms                                                                     | 40.9 ms: 1.16x faster                                                      |
| sqlglot_transpile          | 1.10 ms                                                                     | 961 us: 1.15x faster                                                       |
| generators                 | 17.3 ms                                                                     | 15.1 ms: 1.15x faster                                                      |
| scimark_sparse_mat_mult    | 2.76 ms                                                                     | 2.42 ms: 1.14x faster                                                      |
| deepcopy                   | 185 us                                                                      | 163 us: 1.13x faster                                                       |
| nqueens                    | 64.8 ms                                                                     | 57.4 ms: 1.13x faster                                                      |
| raytrace                   | 182 ms                                                                      | 162 ms: 1.12x faster                                                       |
| deepcopy_reduce            | 1.95 us                                                                     | 1.73 us: 1.12x faster                                                      |
| genshi_xml                 | 34.1 ms                                                                     | 30.5 ms: 1.12x faster                                                      |
| sqlglot_normalize          | 201 ms                                                                      | 181 ms: 1.11x faster                                                       |
| pycparser                  | 753 ms                                                                      | 680 ms: 1.11x faster                                                       |
| async_tree_io              | 401 ms                                                                      | 363 ms: 1.11x faster                                                       |
| bpe_tokeniser              | 3.34 sec                                                                    | 3.03 sec: 1.10x faster                                                     |
| django_template            | 25.7 ms                                                                     | 23.3 ms: 1.10x faster                                                      |
| async_tree_none            | 177 ms                                                                      | 161 ms: 1.10x faster                                                       |
| xml_etree_generate         | 67.6 ms                                                                     | 61.4 ms: 1.10x faster                                                      |
| logging_simple             | 6.41 us                                                                     | 5.84 us: 1.10x faster                                                      |
| sqlglot_optimize           | 37.0 ms                                                                     | 33.9 ms: 1.09x faster                                                      |
| async_generators           | 254 ms                                                                      | 233 ms: 1.09x faster                                                       |
| html5lib                   | 39.8 ms                                                                     | 36.6 ms: 1.09x faster                                                      |
| xml_etree_iterparse        | 71.0 ms                                                                     | 65.6 ms: 1.08x faster                                                      |
| logging_format             | 6.82 us                                                                     | 6.33 us: 1.08x faster                                                      |
| sympy_str                  | 182 ms                                                                      | 169 ms: 1.08x faster                                                       |
| typing_runtime_protocols   | 115 us                                                                      | 107 us: 1.08x faster                                                       |
| async_tree_none_tg         | 166 ms                                                                      | 154 ms: 1.08x faster                                                       |
| async_tree_io_tg           | 391 ms                                                                      | 364 ms: 1.07x faster                                                       |
| async_tree_memoization     | 218 ms                                                                      | 203 ms: 1.07x faster                                                       |
| sympy_expand               | 314 ms                                                                      | 293 ms: 1.07x faster                                                       |
| sympy_integrate            | 13.7 ms                                                                     | 12.9 ms: 1.07x faster                                                      |
| 2to3                       | 239 ms                                                                      | 225 ms: 1.06x faster                                                       |
| json_dumps                 | 7.79 ms                                                                     | 7.33 ms: 1.06x faster                                                      |
| sphinx                     | 706 ms                                                                      | 666 ms: 1.06x faster                                                       |
| dulwich_log                | 42.3 ms                                                                     | 39.9 ms: 1.06x faster                                                      |
| sympy_sum                  | 92.0 ms                                                                     | 87.0 ms: 1.06x faster                                                      |
| many_optionals             | 460 us                                                                      | 436 us: 1.06x faster                                                       |
| meteor_contest             | 75.4 ms                                                                     | 71.6 ms: 1.05x faster                                                      |
| telco                      | 5.18 ms                                                                     | 4.92 ms: 1.05x faster                                                      |
| docutils                   | 1.79 sec                                                                    | 1.71 sec: 1.05x faster                                                     |
| coverage                   | 53.1 ms                                                                     | 50.5 ms: 1.05x faster                                                      |
| pylint                     | 206 ms                                                                      | 196 ms: 1.05x faster                                                       |
| bench_thread_pool          | 878 us                                                                      | 840 us: 1.05x faster                                                       |
| subparsers                 | 16.5 ms                                                                     | 15.8 ms: 1.04x faster                                                      |
| xml_etree_parse            | 102 ms                                                                      | 97.9 ms: 1.04x faster                                                      |
| mdp                        | 1.68 sec                                                                    | 1.62 sec: 1.03x faster                                                     |
| json                       | 3.67 ms                                                                     | 3.58 ms: 1.02x faster                                                      |
| async_tree_cpu_io_mixed_tg | 373 ms                                                                      | 365 ms: 1.02x faster                                                       |
| regex_dna                  | 142 ms                                                                      | 139 ms: 1.02x faster                                                       |
| connected_components       | 329 ms                                                                      | 324 ms: 1.02x faster                                                       |
| sqlite_synth               | 1.72 us                                                                     | 1.69 us: 1.02x faster                                                      |
| shortest_path              | 352 ms                                                                      | 348 ms: 1.01x faster                                                       |
| async_tree_cpu_io_mixed    | 373 ms                                                                      | 369 ms: 1.01x faster                                                       |
| regex_effbot               | 1.98 ms                                                                     | 1.99 ms: 1.00x slower                                                      |
| gc_traversal               | 2.54 ms                                                                     | 2.85 ms: 1.13x slower                                                      |
| Geometric mean             | (ref)                                                                       | 1.11x faster                                                               |

Benchmark hidden because not significant (12): regex_v8, async_tree_memoization_tg, k_core, python_startup_no_site, python_startup, pathlib, pidigits, bench_mp_pool, asyncio_websockets, thrift, create_gc_cycles, json_loads

- Geometric mean (including insignificant results): 1.108x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: unknown