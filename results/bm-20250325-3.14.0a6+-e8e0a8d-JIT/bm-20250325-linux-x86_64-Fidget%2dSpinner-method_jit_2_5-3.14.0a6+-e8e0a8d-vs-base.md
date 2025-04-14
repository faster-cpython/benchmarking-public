# Results vs. base

- fork: Fidget-Spinner
- ref: method_jit_2_5
- machine: linux-x86_64
- commit hash: e8e0a8d
- commit date: 2025-03-25
- overall geometric mean: 1.022x slower
- HPT reliability: 99.90%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250323-linux-x86_64-python-ef06508f8ef1d2943b2f-3.14.0a6+-ef06508 | bm-20250325-linux-x86_64-Fidget%2dSpinner-method_jit_2_5-3.14.0a6+-e8e0a8d |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 264 ms                                                                 | 259 ms: 1.02x faster                                                       |
| html5lib       | 62.8 ms                                                                | 62.2 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                               |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20250323-linux-x86_64-python-ef06508f8ef1d2943b2f-3.14.0a6+-ef06508 | bm-20250325-linux-x86_64-Fidget%2dSpinner-method_jit_2_5-3.14.0a6+-e8e0a8d |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_generators       | 416 ms                                                                 | 406 ms: 1.03x faster                                                       |
| async_tree_none_tg     | 251 ms                                                                 | 254 ms: 1.01x slower                                                       |
| async_tree_memoization | 316 ms                                                                 | 319 ms: 1.01x slower                                                       |
| coroutines             | 23.4 ms                                                                | 24.9 ms: 1.06x slower                                                      |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                               |

Benchmark hidden because not significant (7): async_tree_io_tg, async_tree_cpu_io_mixed_tg, asyncio_websockets, async_tree_cpu_io_mixed, async_tree_io, async_tree_none, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250323-linux-x86_64-python-ef06508f8ef1d2943b2f-3.14.0a6+-ef06508 | bm-20250325-linux-x86_64-Fidget%2dSpinner-method_jit_2_5-3.14.0a6+-e8e0a8d |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                                 | 187 ms: 1.01x slower                                                       |
| float          | 65.2 ms                                                                | 70.4 ms: 1.08x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                               |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250323-linux-x86_64-python-ef06508f8ef1d2943b2f-3.14.0a6+-ef06508 | bm-20250325-linux-x86_64-Fidget%2dSpinner-method_jit_2_5-3.14.0a6+-e8e0a8d |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.3 ms                                                                | 23.5 ms: 1.01x slower                                                      |
| regex_compile  | 127 ms                                                                 | 130 ms: 1.03x slower                                                       |
| regex_dna      | 211 ms                                                                 | 224 ms: 1.06x slower                                                       |
| regex_effbot   | 3.17 ms                                                                | 3.47 ms: 1.09x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.05x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250323-linux-x86_64-python-ef06508f8ef1d2943b2f-3.14.0a6+-ef06508 | bm-20250325-linux-x86_64-Fidget%2dSpinner-method_jit_2_5-3.14.0a6+-e8e0a8d |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 11.6 ms                                                                | 11.4 ms: 1.02x faster                                                      |
| json_loads           | 29.7 us                                                                | 30.0 us: 1.01x slower                                                      |
| xml_etree_iterparse  | 97.7 ms                                                                | 99.0 ms: 1.01x slower                                                      |
| xml_etree_parse      | 140 ms                                                                 | 142 ms: 1.02x slower                                                       |
| pickle_pure_python   | 324 us                                                                 | 331 us: 1.02x slower                                                       |
| unpickle_pure_python | 214 us                                                                 | 224 us: 1.05x slower                                                       |
| xml_etree_process    | 55.8 ms                                                                | 59.9 ms: 1.07x slower                                                      |
| xml_etree_generate   | 79.7 ms                                                                | 85.7 ms: 1.08x slower                                                      |
| tomli_loads          | 1.86 sec                                                               | 2.04 sec: 1.09x slower                                                     |
| Geometric mean       | (ref)                                                                  | 1.04x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250323-linux-x86_64-python-ef06508f8ef1d2943b2f-3.14.0a6+-ef06508 | bm-20250325-linux-x86_64-Fidget%2dSpinner-method_jit_2_5-3.14.0a6+-e8e0a8d |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 13.1 ms                                                                | 13.1 ms: 1.00x slower                                                      |
| python_startup_no_site | 8.18 ms                                                                | 8.21 ms: 1.00x slower                                                      |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250323-linux-x86_64-python-ef06508f8ef1d2943b2f-3.14.0a6+-ef06508 | bm-20250325-linux-x86_64-Fidget%2dSpinner-method_jit_2_5-3.14.0a6+-e8e0a8d |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 50.0 ms                                                                | 50.6 ms: 1.01x slower                                                      |
| django_template | 31.9 ms                                                                | 32.7 ms: 1.03x slower                                                      |
| genshi_text     | 21.2 ms                                                                | 22.0 ms: 1.04x slower                                                      |
| mako            | 11.0 ms                                                                | 12.0 ms: 1.09x slower                                                      |
| Geometric mean  | (ref)                                                                  | 1.04x slower                                                               |

All benchmarks:
===============

| Benchmark                | bm-20250323-linux-x86_64-python-ef06508f8ef1d2943b2f-3.14.0a6+-ef06508 | bm-20250325-linux-x86_64-Fidget%2dSpinner-method_jit_2_5-3.14.0a6+-e8e0a8d |
|--------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| go                       | 129 ms                                                                 | 121 ms: 1.07x faster                                                       |
| connected_components     | 464 ms                                                                 | 441 ms: 1.05x faster                                                       |
| async_generators         | 416 ms                                                                 | 406 ms: 1.03x faster                                                       |
| fannkuch                 | 423 ms                                                                 | 412 ms: 1.02x faster                                                       |
| scimark_sparse_mat_mult  | 4.79 ms                                                                | 4.68 ms: 1.02x faster                                                      |
| hexiom                   | 6.83 ms                                                                | 6.68 ms: 1.02x faster                                                      |
| typing_runtime_protocols | 166 us                                                                 | 163 us: 1.02x faster                                                       |
| 2to3                     | 264 ms                                                                 | 259 ms: 1.02x faster                                                       |
| sympy_expand             | 474 ms                                                                 | 466 ms: 1.02x faster                                                       |
| json_dumps               | 11.6 ms                                                                | 11.4 ms: 1.02x faster                                                      |
| scimark_lu               | 119 ms                                                                 | 117 ms: 1.01x faster                                                       |
| crypto_pyaes             | 78.9 ms                                                                | 77.8 ms: 1.01x faster                                                      |
| sqlglot_v2_optimize      | 54.2 ms                                                                | 53.6 ms: 1.01x faster                                                      |
| dulwich_log              | 60.4 ms                                                                | 59.8 ms: 1.01x faster                                                      |
| html5lib                 | 62.8 ms                                                                | 62.2 ms: 1.01x faster                                                      |
| deepcopy                 | 263 us                                                                 | 261 us: 1.01x faster                                                       |
| pathlib                  | 17.0 ms                                                                | 16.8 ms: 1.01x faster                                                      |
| scimark_fft              | 318 ms                                                                 | 315 ms: 1.01x faster                                                       |
| sqlalchemy_declarative   | 133 ms                                                                 | 132 ms: 1.01x faster                                                       |
| many_optionals           | 968 us                                                                 | 962 us: 1.01x faster                                                       |
| gc_traversal             | 4.66 ms                                                                | 4.65 ms: 1.00x faster                                                      |
| python_startup           | 13.1 ms                                                                | 13.1 ms: 1.00x slower                                                      |
| python_startup_no_site   | 8.18 ms                                                                | 8.21 ms: 1.00x slower                                                      |
| sympy_integrate          | 20.1 ms                                                                | 20.1 ms: 1.00x slower                                                      |
| bench_thread_pool        | 879 us                                                                 | 883 us: 1.00x slower                                                       |
| pidigits                 | 186 ms                                                                 | 187 ms: 1.01x slower                                                       |
| mdp                      | 2.48 sec                                                               | 2.50 sec: 1.01x slower                                                     |
| chaos                    | 60.5 ms                                                                | 61.1 ms: 1.01x slower                                                      |
| async_tree_none_tg       | 251 ms                                                                 | 254 ms: 1.01x slower                                                       |
| regex_v8                 | 23.3 ms                                                                | 23.5 ms: 1.01x slower                                                      |
| json_loads               | 29.7 us                                                                | 30.0 us: 1.01x slower                                                      |
| logging_format           | 6.26 us                                                                | 6.33 us: 1.01x slower                                                      |
| async_tree_memoization   | 316 ms                                                                 | 319 ms: 1.01x slower                                                       |
| sqlite_synth             | 2.73 us                                                                | 2.76 us: 1.01x slower                                                      |
| genshi_xml               | 50.0 ms                                                                | 50.6 ms: 1.01x slower                                                      |
| subparsers               | 21.0 ms                                                                | 21.2 ms: 1.01x slower                                                      |
| xml_etree_iterparse      | 97.7 ms                                                                | 99.0 ms: 1.01x slower                                                      |
| logging_silent           | 99.2 ns                                                                | 101 ns: 1.01x slower                                                       |
| scimark_sor              | 120 ms                                                                 | 122 ms: 1.02x slower                                                       |
| bpe_tokeniser            | 4.60 sec                                                               | 4.67 sec: 1.02x slower                                                     |
| nqueens                  | 84.4 ms                                                                | 85.9 ms: 1.02x slower                                                      |
| json                     | 5.25 ms                                                                | 5.34 ms: 1.02x slower                                                      |
| sqlalchemy_imperative    | 16.9 ms                                                                | 17.2 ms: 1.02x slower                                                      |
| xml_etree_parse          | 140 ms                                                                 | 142 ms: 1.02x slower                                                       |
| pickle_pure_python       | 324 us                                                                 | 331 us: 1.02x slower                                                       |
| sqlglot_v2_transpile     | 1.60 ms                                                                | 1.64 ms: 1.02x slower                                                      |
| sqlglot_v2_parse         | 1.29 ms                                                                | 1.32 ms: 1.02x slower                                                      |
| generators               | 28.6 ms                                                                | 29.2 ms: 1.02x slower                                                      |
| django_template          | 31.9 ms                                                                | 32.7 ms: 1.03x slower                                                      |
| regex_compile            | 127 ms                                                                 | 130 ms: 1.03x slower                                                       |
| logging_simple           | 5.57 us                                                                | 5.72 us: 1.03x slower                                                      |
| sympy_str                | 275 ms                                                                 | 282 ms: 1.03x slower                                                       |
| telco                    | 7.77 ms                                                                | 7.99 ms: 1.03x slower                                                      |
| sympy_sum                | 152 ms                                                                 | 157 ms: 1.03x slower                                                       |
| pyflate                  | 448 ms                                                                 | 464 ms: 1.04x slower                                                       |
| pycparser                | 1.15 sec                                                               | 1.19 sec: 1.04x slower                                                     |
| genshi_text              | 21.2 ms                                                                | 22.0 ms: 1.04x slower                                                      |
| spectral_norm            | 95.4 ms                                                                | 99.7 ms: 1.04x slower                                                      |
| unpickle_pure_python     | 214 us                                                                 | 224 us: 1.05x slower                                                       |
| regex_dna                | 211 ms                                                                 | 224 ms: 1.06x slower                                                       |
| deepcopy_memo            | 28.9 us                                                                | 30.7 us: 1.06x slower                                                      |
| coroutines               | 23.4 ms                                                                | 24.9 ms: 1.06x slower                                                      |
| raytrace                 | 270 ms                                                                 | 288 ms: 1.06x slower                                                       |
| thrift                   | 773 us                                                                 | 823 us: 1.07x slower                                                       |
| pprint_pformat           | 1.56 sec                                                               | 1.66 sec: 1.07x slower                                                     |
| xml_etree_process        | 55.8 ms                                                                | 59.9 ms: 1.07x slower                                                      |
| xml_etree_generate       | 79.7 ms                                                                | 85.7 ms: 1.08x slower                                                      |
| float                    | 65.2 ms                                                                | 70.4 ms: 1.08x slower                                                      |
| pprint_safe_repr         | 755 ms                                                                 | 815 ms: 1.08x slower                                                       |
| deltablue                | 3.08 ms                                                                | 3.32 ms: 1.08x slower                                                      |
| mako                     | 11.0 ms                                                                | 12.0 ms: 1.09x slower                                                      |
| coverage                 | 85.0 ms                                                                | 92.9 ms: 1.09x slower                                                      |
| tomli_loads              | 1.86 sec                                                               | 2.04 sec: 1.09x slower                                                     |
| regex_effbot             | 3.17 ms                                                                | 3.47 ms: 1.09x slower                                                      |
| comprehensions           | 18.9 us                                                                | 20.8 us: 1.10x slower                                                      |
| richards_super           | 41.1 ms                                                                | 53.0 ms: 1.29x slower                                                      |
| richards                 | 36.1 ms                                                                | 46.6 ms: 1.29x slower                                                      |
| Geometric mean           | (ref)                                                                  | 1.02x slower                                                               |

Benchmark hidden because not significant (18): nbody, shortest_path, k_core, async_tree_io_tg, async_tree_cpu_io_mixed_tg, asyncio_websockets, async_tree_cpu_io_mixed, deepcopy_reduce, create_gc_cycles, bench_mp_pool, sqlglot_v2_normalize, async_tree_io, meteor_contest, sphinx, scimark_monte_carlo, async_tree_none, async_tree_memoization_tg, pylint
Ignored benchmarks (1) of results/bm-20250323-3.14.0a6+-ef06508-JIT/bm-20250323-linux-x86_64-python-ef06508f8ef1d2943b2f-3.14.0a6+-ef06508.json: docutils

- Geometric mean (including insignificant results): 1.022x slower

# HPT report

- Reliability score: 99.90% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x