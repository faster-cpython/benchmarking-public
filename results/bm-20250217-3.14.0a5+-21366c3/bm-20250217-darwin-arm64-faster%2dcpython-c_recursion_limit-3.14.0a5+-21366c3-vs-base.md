# Results vs. base

- fork: faster-cpython
- ref: c_recursion_limit
- machine: darwin-arm64
- commit hash: 21366c3
- commit date: 2025-02-17
- overall geometric mean: 1.002x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250214-darwin-arm64-python-1775091dc163d1fa76c3-3.14.0a5+-1775091 | bm-20250217-darwin-arm64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 178 ms                                                                 | 205 ms: 1.15x slower                                                          |
| html5lib       | 34.7 ms                                                                | 32.9 ms: 1.05x faster                                                         |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                                  |

Benchmark hidden because not significant (2): docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20250214-darwin-arm64-python-1775091dc163d1fa76c3-3.14.0a5+-1775091 | bm-20250217-darwin-arm64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_memoization | 225 ms                                                                 | 221 ms: 1.02x faster                                                          |
| async_tree_none_tg     | 174 ms                                                                 | 173 ms: 1.01x faster                                                          |
| async_generators       | 271 ms                                                                 | 269 ms: 1.01x faster                                                          |
| async_tree_io_tg       | 406 ms                                                                 | 404 ms: 1.01x faster                                                          |
| asyncio_websockets     | 243 ms                                                                 | 242 ms: 1.00x faster                                                          |
| async_tree_io          | 420 ms                                                                 | 424 ms: 1.01x slower                                                          |
| async_tree_none        | 181 ms                                                                 | 184 ms: 1.02x slower                                                          |
| async_tree_eager       | 71.8 ms                                                                | 74.2 ms: 1.03x slower                                                         |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                                  |

Benchmark hidden because not significant (11): async_tree_eager_io, async_tree_eager_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_eager_memoization, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_cpu_io_mixed, coroutines, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250214-darwin-arm64-python-1775091dc163d1fa76c3-3.14.0a5+-1775091 | bm-20250217-darwin-arm64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody          | 95.2 ms                                                                | 91.9 ms: 1.04x faster                                                         |
| float          | 54.7 ms                                                                | 54.2 ms: 1.01x faster                                                         |
| pidigits       | 284 ms                                                                 | 284 ms: 1.00x slower                                                          |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250214-darwin-arm64-python-1775091dc163d1fa76c3-3.14.0a5+-1775091 | bm-20250217-darwin-arm64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_dna      | 144 ms                                                                 | 141 ms: 1.02x faster                                                          |
| regex_compile  | 78.0 ms                                                                | 77.5 ms: 1.01x faster                                                         |
| regex_effbot   | 2.27 ms                                                                | 2.30 ms: 1.02x slower                                                         |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                  |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250214-darwin-arm64-python-1775091dc163d1fa76c3-3.14.0a5+-1775091 | bm-20250217-darwin-arm64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| unpickle_pure_python | 172 us                                                                 | 170 us: 1.01x faster                                                          |
| xml_etree_iterparse  | 75.2 ms                                                                | 74.6 ms: 1.01x faster                                                         |
| pickle_pure_python   | 233 us                                                                 | 232 us: 1.01x faster                                                          |
| json_dumps           | 7.57 ms                                                                | 7.53 ms: 1.00x faster                                                         |
| xml_etree_parse      | 99.6 ms                                                                | 102 ms: 1.02x slower                                                          |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                                  |

Benchmark hidden because not significant (4): json_loads, xml_etree_process, xml_etree_generate, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250214-darwin-arm64-python-1775091dc163d1fa76c3-3.14.0a5+-1775091 | bm-20250217-darwin-arm64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 18.5 ms                                                                | 18.1 ms: 1.02x faster                                                         |
| python_startup_no_site | 13.6 ms                                                                | 13.4 ms: 1.02x faster                                                         |
| Geometric mean         | (ref)                                                                  | 1.02x faster                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250214-darwin-arm64-python-1775091dc163d1fa76c3-3.14.0a5+-1775091 | bm-20250217-darwin-arm64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|-----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| django_template | 24.4 ms                                                                | 24.1 ms: 1.01x faster                                                         |
| genshi_xml      | 34.1 ms                                                                | 33.8 ms: 1.01x faster                                                         |
| genshi_text     | 16.4 ms                                                                | 16.3 ms: 1.01x faster                                                         |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                                  |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                | bm-20250214-darwin-arm64-python-1775091dc163d1fa76c3-3.14.0a5+-1775091 | bm-20250217-darwin-arm64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|--------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| html5lib                 | 34.7 ms                                                                | 32.9 ms: 1.05x faster                                                         |
| nbody                    | 95.2 ms                                                                | 91.9 ms: 1.04x faster                                                         |
| regex_dna                | 144 ms                                                                 | 141 ms: 1.02x faster                                                          |
| typing_runtime_protocols | 103 us                                                                 | 101 us: 1.02x faster                                                          |
| python_startup           | 18.5 ms                                                                | 18.1 ms: 1.02x faster                                                         |
| logging_silent           | 74.6 ns                                                                | 73.4 ns: 1.02x faster                                                         |
| async_tree_memoization   | 225 ms                                                                 | 221 ms: 1.02x faster                                                          |
| shortest_path            | 348 ms                                                                 | 343 ms: 1.02x faster                                                          |
| deepcopy_memo            | 21.2 us                                                                | 20.9 us: 1.02x faster                                                         |
| python_startup_no_site   | 13.6 ms                                                                | 13.4 ms: 1.02x faster                                                         |
| pprint_safe_repr         | 549 ms                                                                 | 542 ms: 1.01x faster                                                          |
| scimark_sor              | 93.9 ms                                                                | 92.7 ms: 1.01x faster                                                         |
| bpe_tokeniser            | 3.24 sec                                                               | 3.20 sec: 1.01x faster                                                        |
| sqlglot_normalize        | 198 ms                                                                 | 196 ms: 1.01x faster                                                          |
| django_template          | 24.4 ms                                                                | 24.1 ms: 1.01x faster                                                         |
| deltablue                | 2.79 ms                                                                | 2.76 ms: 1.01x faster                                                         |
| hexiom                   | 5.32 ms                                                                | 5.26 ms: 1.01x faster                                                         |
| pathlib                  | 23.4 ms                                                                | 23.2 ms: 1.01x faster                                                         |
| deepcopy                 | 168 us                                                                 | 167 us: 1.01x faster                                                          |
| async_tree_none_tg       | 174 ms                                                                 | 173 ms: 1.01x faster                                                          |
| sqlglot_parse            | 896 us                                                                 | 888 us: 1.01x faster                                                          |
| meteor_contest           | 78.6 ms                                                                | 78.0 ms: 1.01x faster                                                         |
| raytrace                 | 214 ms                                                                 | 212 ms: 1.01x faster                                                          |
| genshi_xml               | 34.1 ms                                                                | 33.8 ms: 1.01x faster                                                         |
| unpickle_pure_python     | 172 us                                                                 | 170 us: 1.01x faster                                                          |
| scimark_monte_carlo      | 50.5 ms                                                                | 50.1 ms: 1.01x faster                                                         |
| genshi_text              | 16.4 ms                                                                | 16.3 ms: 1.01x faster                                                         |
| float                    | 54.7 ms                                                                | 54.2 ms: 1.01x faster                                                         |
| xml_etree_iterparse      | 75.2 ms                                                                | 74.6 ms: 1.01x faster                                                         |
| sqlglot_optimize         | 35.8 ms                                                                | 35.6 ms: 1.01x faster                                                         |
| go                       | 95.3 ms                                                                | 94.6 ms: 1.01x faster                                                         |
| logging_format           | 4.09 us                                                                | 4.07 us: 1.01x faster                                                         |
| sympy_expand             | 256 ms                                                                 | 255 ms: 1.01x faster                                                          |
| regex_compile            | 78.0 ms                                                                | 77.5 ms: 1.01x faster                                                         |
| chaos                    | 44.8 ms                                                                | 44.5 ms: 1.01x faster                                                         |
| pickle_pure_python       | 233 us                                                                 | 232 us: 1.01x faster                                                          |
| async_generators         | 271 ms                                                                 | 269 ms: 1.01x faster                                                          |
| async_tree_io_tg         | 406 ms                                                                 | 404 ms: 1.01x faster                                                          |
| mdp                      | 1.56 sec                                                               | 1.56 sec: 1.01x faster                                                        |
| pprint_pformat           | 1.11 sec                                                               | 1.10 sec: 1.01x faster                                                        |
| deepcopy_reduce          | 1.77 us                                                                | 1.76 us: 1.01x faster                                                         |
| richards_super           | 42.9 ms                                                                | 42.7 ms: 1.00x faster                                                         |
| json_dumps               | 7.57 ms                                                                | 7.53 ms: 1.00x faster                                                         |
| spectral_norm            | 78.2 ms                                                                | 77.9 ms: 1.00x faster                                                         |
| logging_simple           | 3.76 us                                                                | 3.75 us: 1.00x faster                                                         |
| gc_traversal             | 3.12 ms                                                                | 3.11 ms: 1.00x faster                                                         |
| richards                 | 40.0 ms                                                                | 39.8 ms: 1.00x faster                                                         |
| comprehensions           | 13.0 us                                                                | 13.0 us: 1.00x faster                                                         |
| sympy_integrate          | 12.3 ms                                                                | 12.3 ms: 1.00x faster                                                         |
| sqlalchemy_declarative   | 62.7 ms                                                                | 62.5 ms: 1.00x faster                                                         |
| dulwich_log              | 30.1 ms                                                                | 30.0 ms: 1.00x faster                                                         |
| asyncio_websockets       | 243 ms                                                                 | 242 ms: 1.00x faster                                                          |
| scimark_fft              | 198 ms                                                                 | 198 ms: 1.00x slower                                                          |
| pidigits                 | 284 ms                                                                 | 284 ms: 1.00x slower                                                          |
| crypto_pyaes             | 58.5 ms                                                                | 58.6 ms: 1.00x slower                                                         |
| scimark_sparse_mat_mult  | 3.08 ms                                                                | 3.08 ms: 1.00x slower                                                         |
| nqueens                  | 65.5 ms                                                                | 65.7 ms: 1.00x slower                                                         |
| sqlglot_transpile        | 1.07 ms                                                                | 1.08 ms: 1.00x slower                                                         |
| telco                    | 4.76 ms                                                                | 4.78 ms: 1.00x slower                                                         |
| sqlite_synth             | 1.53 us                                                                | 1.54 us: 1.01x slower                                                         |
| async_tree_io            | 420 ms                                                                 | 424 ms: 1.01x slower                                                          |
| fannkuch                 | 291 ms                                                                 | 294 ms: 1.01x slower                                                          |
| regex_effbot             | 2.27 ms                                                                | 2.30 ms: 1.02x slower                                                         |
| async_tree_none          | 181 ms                                                                 | 184 ms: 1.02x slower                                                          |
| xml_etree_parse          | 99.6 ms                                                                | 102 ms: 1.02x slower                                                          |
| async_tree_eager         | 71.8 ms                                                                | 74.2 ms: 1.03x slower                                                         |
| 2to3                     | 178 ms                                                                 | 205 ms: 1.15x slower                                                          |
| Geometric mean           | (ref)                                                                  | 1.00x faster                                                                  |

Benchmark hidden because not significant (37): async_tree_eager_io, async_tree_eager_tg, subparsers, coverage, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_eager_memoization, async_tree_eager_io_tg, json_loads, bench_mp_pool, sympy_sum, k_core, async_tree_eager_memoization_tg, pylint, pyflate, sqlalchemy_imperative, bench_thread_pool, pycparser, async_tree_cpu_io_mixed, many_optionals, sphinx, regex_v8, mako, sympy_str, thrift, scimark_lu, xml_etree_process, coroutines, json, create_gc_cycles, xml_etree_generate, docutils, generators, tomli_loads, async_tree_eager_cpu_io_mixed, connected_components, async_tree_eager_cpu_io_mixed_tg
Ignored benchmarks (1) of results/bm-20250214-3.14.0a5+-1775091/bm-20250214-darwin-arm64-python-1775091dc163d1fa76c3-3.14.0a5+-1775091.json: dask

- Geometric mean (including insignificant results): 1.002x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x