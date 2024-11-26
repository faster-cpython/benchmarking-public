# Results vs. base

- fork: brandtbucher
- ref: optimize_off
- machine: linux-x86_64
- commit hash: 9808234
- commit date: 2024-11-17
- overall geometric mean: 1.008x slower
- HPT reliability: 99.76%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241116-linux-x86_64-python-2313f8421080ceb3343c-3.14.0a1+-2313f84 | bm-20241117-linux-x86_64-brandtbucher-optimize_off-3.14.0a1+-9808234 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 281 ms                                                                 | 283 ms: 1.01x slower                                                 |
| docutils       | 2.93 sec                                                               | 3.13 sec: 1.07x slower                                               |
| html5lib       | 66.3 ms                                                                | 68.6 ms: 1.03x slower                                                |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                         |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20241116-linux-x86_64-python-2313f8421080ceb3343c-3.14.0a1+-2313f84 | bm-20241117-linux-x86_64-brandtbucher-optimize_off-3.14.0a1+-9808234 |
|------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_none  | 337 ms                                                                 | 333 ms: 1.01x faster                                                 |
| async_tree_io_tg | 988 ms                                                                 | 977 ms: 1.01x faster                                                 |
| coroutines       | 22.8 ms                                                                | 22.6 ms: 1.01x faster                                                |
| async_generators | 451 ms                                                                 | 454 ms: 1.01x slower                                                 |
| Geometric mean   | (ref)                                                                  | 1.00x faster                                                         |

Benchmark hidden because not significant (7): async_tree_io, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_none_tg, asyncio_websockets, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241116-linux-x86_64-python-2313f8421080ceb3343c-3.14.0a1+-2313f84 | bm-20241117-linux-x86_64-brandtbucher-optimize_off-3.14.0a1+-9808234 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| pidigits       | 186 ms                                                                 | 187 ms: 1.00x slower                                                 |
| float          | 76.5 ms                                                                | 77.2 ms: 1.01x slower                                                |
| nbody          | 82.4 ms                                                                | 84.5 ms: 1.02x slower                                                |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241116-linux-x86_64-python-2313f8421080ceb3343c-3.14.0a1+-2313f84 | bm-20241117-linux-x86_64-brandtbucher-optimize_off-3.14.0a1+-9808234 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_v8       | 25.2 ms                                                                | 25.3 ms: 1.00x slower                                                |
| regex_effbot   | 3.66 ms                                                                | 3.73 ms: 1.02x slower                                                |
| regex_dna      | 211 ms                                                                 | 215 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                         |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241116-linux-x86_64-python-2313f8421080ceb3343c-3.14.0a1+-2313f84 | bm-20241117-linux-x86_64-brandtbucher-optimize_off-3.14.0a1+-9808234 |
|---------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_iterparse | 101 ms                                                                 | 99.7 ms: 1.02x faster                                                |
| tomli_loads         | 1.94 sec                                                               | 1.92 sec: 1.01x faster                                               |
| xml_etree_generate  | 79.5 ms                                                                | 78.7 ms: 1.01x faster                                                |
| json_loads          | 26.5 us                                                                | 26.6 us: 1.00x slower                                                |
| xml_etree_process   | 55.6 ms                                                                | 56.2 ms: 1.01x slower                                                |
| json_dumps          | 11.2 ms                                                                | 11.4 ms: 1.01x slower                                                |
| xml_etree_parse     | 147 ms                                                                 | 149 ms: 1.01x slower                                                 |
| pickle_pure_python  | 322 us                                                                 | 328 us: 1.02x slower                                                 |
| Geometric mean      | (ref)                                                                  | 1.00x slower                                                         |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241116-linux-x86_64-python-2313f8421080ceb3343c-3.14.0a1+-2313f84 | bm-20241117-linux-x86_64-brandtbucher-optimize_off-3.14.0a1+-9808234 |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 7.16 ms                                                                | 7.09 ms: 1.01x faster                                                |
| python_startup         | 12.9 ms                                                                | 12.8 ms: 1.01x faster                                                |
| Geometric mean         | (ref)                                                                  | 1.01x faster                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241116-linux-x86_64-python-2313f8421080ceb3343c-3.14.0a1+-2313f84 | bm-20241117-linux-x86_64-brandtbucher-optimize_off-3.14.0a1+-9808234 |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_text     | 25.2 ms                                                                | 24.8 ms: 1.02x faster                                                |
| django_template | 33.8 ms                                                                | 34.3 ms: 1.02x slower                                                |
| mako            | 10.1 ms                                                                | 10.3 ms: 1.03x slower                                                |
| genshi_xml      | 57.8 ms                                                                | 60.8 ms: 1.05x slower                                                |
| Geometric mean  | (ref)                                                                  | 1.02x slower                                                         |

All benchmarks:
===============

| Benchmark                | bm-20241116-linux-x86_64-python-2313f8421080ceb3343c-3.14.0a1+-2313f84 | bm-20241117-linux-x86_64-brandtbucher-optimize_off-3.14.0a1+-9808234 |
|--------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| gc_traversal             | 4.81 ms                                                                | 4.52 ms: 1.06x faster                                                |
| pathlib                  | 16.2 ms                                                                | 15.9 ms: 1.02x faster                                                |
| genshi_text              | 25.2 ms                                                                | 24.8 ms: 1.02x faster                                                |
| xml_etree_iterparse      | 101 ms                                                                 | 99.7 ms: 1.02x faster                                                |
| tomli_loads              | 1.94 sec                                                               | 1.92 sec: 1.01x faster                                               |
| async_tree_none          | 337 ms                                                                 | 333 ms: 1.01x faster                                                 |
| bench_mp_pool            | 85.5 ms                                                                | 84.5 ms: 1.01x faster                                                |
| async_tree_io_tg         | 988 ms                                                                 | 977 ms: 1.01x faster                                                 |
| telco                    | 7.50 ms                                                                | 7.42 ms: 1.01x faster                                                |
| python_startup_no_site   | 7.16 ms                                                                | 7.09 ms: 1.01x faster                                                |
| xml_etree_generate       | 79.5 ms                                                                | 78.7 ms: 1.01x faster                                                |
| create_gc_cycles         | 2.70 ms                                                                | 2.68 ms: 1.01x faster                                                |
| python_startup           | 12.9 ms                                                                | 12.8 ms: 1.01x faster                                                |
| coroutines               | 22.8 ms                                                                | 22.6 ms: 1.01x faster                                                |
| bench_thread_pool        | 899 us                                                                 | 895 us: 1.01x faster                                                 |
| sympy_expand             | 510 ms                                                                 | 508 ms: 1.00x faster                                                 |
| shortest_path            | 482 ms                                                                 | 481 ms: 1.00x faster                                                 |
| pidigits                 | 186 ms                                                                 | 187 ms: 1.00x slower                                                 |
| connected_components     | 438 ms                                                                 | 439 ms: 1.00x slower                                                 |
| regex_v8                 | 25.2 ms                                                                | 25.3 ms: 1.00x slower                                                |
| sympy_integrate          | 23.7 ms                                                                | 23.8 ms: 1.00x slower                                                |
| sqlalchemy_declarative   | 147 ms                                                                 | 147 ms: 1.00x slower                                                 |
| bpe_tokeniser            | 4.46 sec                                                               | 4.48 sec: 1.00x slower                                               |
| json_loads               | 26.5 us                                                                | 26.6 us: 1.00x slower                                                |
| sqlglot_normalize        | 115 ms                                                                 | 116 ms: 1.01x slower                                                 |
| 2to3                     | 281 ms                                                                 | 283 ms: 1.01x slower                                                 |
| hexiom                   | 7.15 ms                                                                | 7.19 ms: 1.01x slower                                                |
| sqlglot_parse            | 1.33 ms                                                                | 1.34 ms: 1.01x slower                                                |
| sqlglot_optimize         | 60.2 ms                                                                | 60.6 ms: 1.01x slower                                                |
| logging_simple           | 5.60 us                                                                | 5.64 us: 1.01x slower                                                |
| scimark_monte_carlo      | 64.0 ms                                                                | 64.6 ms: 1.01x slower                                                |
| async_generators         | 451 ms                                                                 | 454 ms: 1.01x slower                                                 |
| generators               | 36.0 ms                                                                | 36.4 ms: 1.01x slower                                                |
| subparsers               | 21.2 ms                                                                | 21.4 ms: 1.01x slower                                                |
| float                    | 76.5 ms                                                                | 77.2 ms: 1.01x slower                                                |
| thrift                   | 787 us                                                                 | 795 us: 1.01x slower                                                 |
| xml_etree_process        | 55.6 ms                                                                | 56.2 ms: 1.01x slower                                                |
| deepcopy                 | 269 us                                                                 | 272 us: 1.01x slower                                                 |
| json_dumps               | 11.2 ms                                                                | 11.4 ms: 1.01x slower                                                |
| sqlglot_transpile        | 1.70 ms                                                                | 1.72 ms: 1.01x slower                                                |
| logging_format           | 6.17 us                                                                | 6.24 us: 1.01x slower                                                |
| comprehensions           | 17.6 us                                                                | 17.8 us: 1.01x slower                                                |
| nqueens                  | 89.6 ms                                                                | 90.7 ms: 1.01x slower                                                |
| xml_etree_parse          | 147 ms                                                                 | 149 ms: 1.01x slower                                                 |
| sqlite_synth             | 2.79 us                                                                | 2.83 us: 1.01x slower                                                |
| scimark_fft              | 320 ms                                                                 | 325 ms: 1.01x slower                                                 |
| coverage                 | 83.5 ms                                                                | 84.7 ms: 1.01x slower                                                |
| django_template          | 33.8 ms                                                                | 34.3 ms: 1.02x slower                                                |
| dulwich_log              | 67.5 ms                                                                | 68.6 ms: 1.02x slower                                                |
| mdp                      | 2.59 sec                                                               | 2.63 sec: 1.02x slower                                               |
| many_optionals           | 1.05 ms                                                                | 1.07 ms: 1.02x slower                                                |
| pickle_pure_python       | 322 us                                                                 | 328 us: 1.02x slower                                                 |
| regex_effbot             | 3.66 ms                                                                | 3.73 ms: 1.02x slower                                                |
| regex_dna                | 211 ms                                                                 | 215 ms: 1.02x slower                                                 |
| logging_silent           | 98.9 ns                                                                | 101 ns: 1.02x slower                                                 |
| go                       | 133 ms                                                                 | 136 ms: 1.02x slower                                                 |
| scimark_sparse_mat_mult  | 4.54 ms                                                                | 4.64 ms: 1.02x slower                                                |
| raytrace                 | 285 ms                                                                 | 292 ms: 1.02x slower                                                 |
| typing_runtime_protocols | 166 us                                                                 | 170 us: 1.02x slower                                                 |
| deltablue                | 3.31 ms                                                                | 3.39 ms: 1.02x slower                                                |
| nbody                    | 82.4 ms                                                                | 84.5 ms: 1.02x slower                                                |
| mako                     | 10.1 ms                                                                | 10.3 ms: 1.03x slower                                                |
| json                     | 4.89 ms                                                                | 5.03 ms: 1.03x slower                                                |
| scimark_sor              | 119 ms                                                                 | 122 ms: 1.03x slower                                                 |
| html5lib                 | 66.3 ms                                                                | 68.6 ms: 1.03x slower                                                |
| chaos                    | 59.1 ms                                                                | 61.5 ms: 1.04x slower                                                |
| pycparser                | 1.15 sec                                                               | 1.20 sec: 1.04x slower                                               |
| richards_super           | 46.0 ms                                                                | 48.2 ms: 1.05x slower                                                |
| genshi_xml               | 57.8 ms                                                                | 60.8 ms: 1.05x slower                                                |
| docutils                 | 2.93 sec                                                               | 3.13 sec: 1.07x slower                                               |
| spectral_norm            | 114 ms                                                                 | 122 ms: 1.07x slower                                                 |
| Geometric mean           | (ref)                                                                  | 1.01x slower                                                         |

Benchmark hidden because not significant (26): async_tree_io, richards, sqlalchemy_imperative, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_memoization, fannkuch, async_tree_none_tg, sympy_sum, asyncio_websockets, crypto_pyaes, meteor_contest, sympy_str, pyflate, async_tree_memoization_tg, scimark_lu, deepcopy_reduce, deepcopy_memo, k_core, regex_compile, unpickle_pure_python, pprint_pformat, sphinx, pprint_safe_repr, pylint, djangocms

- Geometric mean (including insignificant results): 1.008x slower
# HPT report

- Reliability score: 99.76% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x