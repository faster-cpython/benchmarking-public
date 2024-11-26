# Results vs. base

- fork: brandtbucher
- ref: warmup_side_8192
- machine: linux-x86_64
- commit hash: b2ebba4
- commit date: 2024-11-21
- overall geometric mean: 1.002x faster
- HPT reliability: 90.79%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241120-linux-x86_64-python-0af4ec30bd2e3a523503-3.14.0a2+-0af4ec3 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_8192-3.14.0a2+-b2ebba4 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 262 ms                                                                 | 260 ms: 1.01x faster                                                     |
| docutils       | 2.83 sec                                                               | 2.75 sec: 1.03x faster                                                   |
| html5lib       | 66.8 ms                                                                | 66.1 ms: 1.01x faster                                                    |
| sphinx         | 1.10 sec                                                               | 1.08 sec: 1.02x faster                                                   |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark      | bm-20241120-linux-x86_64-python-0af4ec30bd2e3a523503-3.14.0a2+-0af4ec3 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_8192-3.14.0a2+-b2ebba4 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| coroutines     | 23.4 ms                                                                | 23.2 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                             |

Benchmark hidden because not significant (10): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_none, async_tree_io_tg, async_tree_io, async_tree_none_tg, async_tree_memoization, asyncio_websockets, async_generators, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241120-linux-x86_64-python-0af4ec30bd2e3a523503-3.14.0a2+-0af4ec3 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_8192-3.14.0a2+-b2ebba4 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 82.5 ms                                                                | 81.4 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                             |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241120-linux-x86_64-python-0af4ec30bd2e3a523503-3.14.0a2+-0af4ec3 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_8192-3.14.0a2+-b2ebba4 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 131 ms                                                                 | 129 ms: 1.02x faster                                                     |
| regex_effbot   | 3.47 ms                                                                | 3.43 ms: 1.01x faster                                                    |
| regex_dna      | 223 ms                                                                 | 224 ms: 1.00x slower                                                     |
| regex_v8       | 25.5 ms                                                                | 26.0 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241120-linux-x86_64-python-0af4ec30bd2e3a523503-3.14.0a2+-0af4ec3 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_8192-3.14.0a2+-b2ebba4 |
|----------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_generate   | 83.0 ms                                                                | 79.1 ms: 1.05x faster                                                    |
| xml_etree_process    | 57.5 ms                                                                | 55.8 ms: 1.03x faster                                                    |
| xml_etree_parse      | 148 ms                                                                 | 146 ms: 1.01x faster                                                     |
| unpickle_pure_python | 193 us                                                                 | 192 us: 1.00x faster                                                     |
| tomli_loads          | 1.95 sec                                                               | 2.00 sec: 1.02x slower                                                   |
| pickle_pure_python   | 319 us                                                                 | 328 us: 1.03x slower                                                     |
| Geometric mean       | (ref)                                                                  | 1.01x faster                                                             |

Benchmark hidden because not significant (3): json_loads, xml_etree_iterparse, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241120-linux-x86_64-python-0af4ec30bd2e3a523503-3.14.0a2+-0af4ec3 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_8192-3.14.0a2+-b2ebba4 |
|------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 12.8 ms                                                                | 12.8 ms: 1.00x slower                                                    |
| python_startup_no_site | 7.05 ms                                                                | 7.06 ms: 1.00x slower                                                    |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241120-linux-x86_64-python-0af4ec30bd2e3a523503-3.14.0a2+-0af4ec3 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_8192-3.14.0a2+-b2ebba4 |
|-----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 25.0 ms                                                                | 24.3 ms: 1.03x faster                                                    |
| mako            | 10.1 ms                                                                | 10.3 ms: 1.02x slower                                                    |
| django_template | 33.0 ms                                                                | 33.6 ms: 1.02x slower                                                    |
| genshi_xml      | 57.1 ms                                                                | 60.4 ms: 1.06x slower                                                    |
| Geometric mean  | (ref)                                                                  | 1.02x slower                                                             |

All benchmarks:
===============

| Benchmark                | bm-20241120-linux-x86_64-python-0af4ec30bd2e3a523503-3.14.0a2+-0af4ec3 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_8192-3.14.0a2+-b2ebba4 |
|--------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_generate       | 83.0 ms                                                                | 79.1 ms: 1.05x faster                                                    |
| go                       | 134 ms                                                                 | 128 ms: 1.04x faster                                                     |
| pylint                   | 284 ms                                                                 | 273 ms: 1.04x faster                                                     |
| scimark_lu               | 115 ms                                                                 | 111 ms: 1.04x faster                                                     |
| xml_etree_process        | 57.5 ms                                                                | 55.8 ms: 1.03x faster                                                    |
| docutils                 | 2.83 sec                                                               | 2.75 sec: 1.03x faster                                                   |
| genshi_text              | 25.0 ms                                                                | 24.3 ms: 1.03x faster                                                    |
| sympy_sum                | 160 ms                                                                 | 155 ms: 1.03x faster                                                     |
| hexiom                   | 7.15 ms                                                                | 6.96 ms: 1.03x faster                                                    |
| sympy_str                | 287 ms                                                                 | 281 ms: 1.02x faster                                                     |
| many_optionals           | 990 us                                                                 | 969 us: 1.02x faster                                                     |
| sqlglot_transpile        | 1.65 ms                                                                | 1.62 ms: 1.02x faster                                                    |
| scimark_sor              | 120 ms                                                                 | 118 ms: 1.02x faster                                                     |
| sphinx                   | 1.10 sec                                                               | 1.08 sec: 1.02x faster                                                   |
| typing_runtime_protocols | 170 us                                                                 | 167 us: 1.02x faster                                                     |
| regex_compile            | 131 ms                                                                 | 129 ms: 1.02x faster                                                     |
| sympy_integrate          | 21.0 ms                                                                | 20.7 ms: 1.02x faster                                                    |
| nqueens                  | 90.8 ms                                                                | 89.4 ms: 1.02x faster                                                    |
| logging_format           | 6.17 us                                                                | 6.08 us: 1.01x faster                                                    |
| dulwich_log              | 68.0 ms                                                                | 67.1 ms: 1.01x faster                                                    |
| sqlalchemy_declarative   | 131 ms                                                                 | 129 ms: 1.01x faster                                                     |
| spectral_norm            | 112 ms                                                                 | 111 ms: 1.01x faster                                                     |
| xml_etree_parse          | 148 ms                                                                 | 146 ms: 1.01x faster                                                     |
| nbody                    | 82.5 ms                                                                | 81.4 ms: 1.01x faster                                                    |
| scimark_sparse_mat_mult  | 4.67 ms                                                                | 4.62 ms: 1.01x faster                                                    |
| sqlglot_parse            | 1.33 ms                                                                | 1.32 ms: 1.01x faster                                                    |
| regex_effbot             | 3.47 ms                                                                | 3.43 ms: 1.01x faster                                                    |
| coroutines               | 23.4 ms                                                                | 23.2 ms: 1.01x faster                                                    |
| html5lib                 | 66.8 ms                                                                | 66.1 ms: 1.01x faster                                                    |
| shortest_path            | 485 ms                                                                 | 481 ms: 1.01x faster                                                     |
| pathlib                  | 16.4 ms                                                                | 16.3 ms: 1.01x faster                                                    |
| connected_components     | 440 ms                                                                 | 437 ms: 1.01x faster                                                     |
| 2to3                     | 262 ms                                                                 | 260 ms: 1.01x faster                                                     |
| sympy_expand             | 482 ms                                                                 | 479 ms: 1.01x faster                                                     |
| comprehensions           | 17.6 us                                                                | 17.5 us: 1.01x faster                                                    |
| bench_thread_pool        | 876 us                                                                 | 871 us: 1.01x faster                                                     |
| unpickle_pure_python     | 193 us                                                                 | 192 us: 1.00x faster                                                     |
| scimark_fft              | 317 ms                                                                 | 316 ms: 1.00x faster                                                     |
| gc_traversal             | 4.35 ms                                                                | 4.35 ms: 1.00x faster                                                    |
| create_gc_cycles         | 2.64 ms                                                                | 2.64 ms: 1.00x slower                                                    |
| python_startup           | 12.8 ms                                                                | 12.8 ms: 1.00x slower                                                    |
| python_startup_no_site   | 7.05 ms                                                                | 7.06 ms: 1.00x slower                                                    |
| regex_dna                | 223 ms                                                                 | 224 ms: 1.00x slower                                                     |
| logging_simple           | 5.55 us                                                                | 5.59 us: 1.01x slower                                                    |
| pyflate                  | 452 ms                                                                 | 455 ms: 1.01x slower                                                     |
| meteor_contest           | 108 ms                                                                 | 109 ms: 1.01x slower                                                     |
| generators               | 35.2 ms                                                                | 35.6 ms: 1.01x slower                                                    |
| telco                    | 7.58 ms                                                                | 7.67 ms: 1.01x slower                                                    |
| pprint_safe_repr         | 720 ms                                                                 | 731 ms: 1.02x slower                                                     |
| json                     | 4.85 ms                                                                | 4.93 ms: 1.02x slower                                                    |
| mako                     | 10.1 ms                                                                | 10.3 ms: 1.02x slower                                                    |
| deepcopy                 | 268 us                                                                 | 273 us: 1.02x slower                                                     |
| django_template          | 33.0 ms                                                                | 33.6 ms: 1.02x slower                                                    |
| subparsers               | 21.0 ms                                                                | 21.4 ms: 1.02x slower                                                    |
| regex_v8                 | 25.5 ms                                                                | 26.0 ms: 1.02x slower                                                    |
| deepcopy_reduce          | 2.69 us                                                                | 2.75 us: 1.02x slower                                                    |
| raytrace                 | 280 ms                                                                 | 286 ms: 1.02x slower                                                     |
| tomli_loads              | 1.95 sec                                                               | 2.00 sec: 1.02x slower                                                   |
| pickle_pure_python       | 319 us                                                                 | 328 us: 1.03x slower                                                     |
| pprint_pformat           | 1.46 sec                                                               | 1.50 sec: 1.03x slower                                                   |
| logging_silent           | 99.4 ns                                                                | 103 ns: 1.03x slower                                                     |
| richards                 | 36.9 ms                                                                | 38.6 ms: 1.05x slower                                                    |
| richards_super           | 42.5 ms                                                                | 44.5 ms: 1.05x slower                                                    |
| genshi_xml               | 57.1 ms                                                                | 60.4 ms: 1.06x slower                                                    |
| mdp                      | 2.59 sec                                                               | 2.78 sec: 1.07x slower                                                   |
| Geometric mean           | (ref)                                                                  | 1.00x faster                                                             |

Benchmark hidden because not significant (32): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, sqlalchemy_imperative, scimark_monte_carlo, async_tree_none, async_tree_io_tg, async_tree_io, json_loads, deltablue, djangocms, sqlglot_normalize, async_tree_none_tg, async_tree_memoization, pidigits, pycparser, xml_etree_iterparse, sqlglot_optimize, asyncio_websockets, json_dumps, sqlite_synth, thrift, deepcopy_memo, async_generators, bpe_tokeniser, chaos, async_tree_memoization_tg, bench_mp_pool, k_core, coverage, float, crypto_pyaes, fannkuch

- Geometric mean (including insignificant results): 1.002x faster
# HPT report

- Reliability score: 90.79% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.99x