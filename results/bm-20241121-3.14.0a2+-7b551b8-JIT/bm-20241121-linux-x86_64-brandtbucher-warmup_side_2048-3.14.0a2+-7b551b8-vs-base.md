# Results vs. base

- fork: brandtbucher
- ref: warmup_side_2048
- machine: linux-x86_64
- commit hash: 7b551b8
- commit date: 2024-11-21
- overall geometric mean: 1.001x slower
- HPT reliability: 73.57%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241120-linux-x86_64-python-0af4ec30bd2e3a523503-3.14.0a2+-0af4ec3 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_2048-3.14.0a2+-7b551b8 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 262 ms                                                                 | 261 ms: 1.00x faster                                                     |
| docutils       | 2.83 sec                                                               | 2.79 sec: 1.01x faster                                                   |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                             |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20241120-linux-x86_64-python-0af4ec30bd2e3a523503-3.14.0a2+-0af4ec3 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_2048-3.14.0a2+-7b551b8 |
|------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| coroutines       | 23.4 ms                                                                | 23.2 ms: 1.01x faster                                                    |
| async_generators | 456 ms                                                                 | 455 ms: 1.00x faster                                                     |
| Geometric mean   | (ref)                                                                  | 1.00x faster                                                             |

Benchmark hidden because not significant (9): async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_none_tg, asyncio_websockets, async_tree_none, async_tree_io, async_tree_io_tg, async_tree_memoization_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241120-linux-x86_64-python-0af4ec30bd2e3a523503-3.14.0a2+-0af4ec3 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_2048-3.14.0a2+-7b551b8 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                                 | 191 ms: 1.02x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                             |

Benchmark hidden because not significant (2): nbody, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241120-linux-x86_64-python-0af4ec30bd2e3a523503-3.14.0a2+-0af4ec3 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_2048-3.14.0a2+-7b551b8 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 131 ms                                                                 | 129 ms: 1.01x faster                                                     |
| regex_effbot   | 3.47 ms                                                                | 3.50 ms: 1.01x slower                                                    |
| regex_dna      | 223 ms                                                                 | 226 ms: 1.01x slower                                                     |
| regex_v8       | 25.5 ms                                                                | 26.0 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241120-linux-x86_64-python-0af4ec30bd2e3a523503-3.14.0a2+-0af4ec3 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_2048-3.14.0a2+-7b551b8 |
|---------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_generate  | 83.0 ms                                                                | 78.5 ms: 1.06x faster                                                    |
| xml_etree_process   | 57.5 ms                                                                | 55.3 ms: 1.04x faster                                                    |
| json_dumps          | 11.2 ms                                                                | 11.1 ms: 1.01x faster                                                    |
| xml_etree_iterparse | 101 ms                                                                 | 100 ms: 1.01x faster                                                     |
| pickle_pure_python  | 319 us                                                                 | 316 us: 1.01x faster                                                     |
| tomli_loads         | 1.95 sec                                                               | 1.97 sec: 1.01x slower                                                   |
| Geometric mean      | (ref)                                                                  | 1.01x faster                                                             |

Benchmark hidden because not significant (3): xml_etree_parse, unpickle_pure_python, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241120-linux-x86_64-python-0af4ec30bd2e3a523503-3.14.0a2+-0af4ec3 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_2048-3.14.0a2+-7b551b8 |
|------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 12.8 ms                                                                | 12.8 ms: 1.00x faster                                                    |
| python_startup_no_site | 7.05 ms                                                                | 7.05 ms: 1.00x slower                                                    |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241120-linux-x86_64-python-0af4ec30bd2e3a523503-3.14.0a2+-0af4ec3 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_2048-3.14.0a2+-7b551b8 |
|-----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 25.0 ms                                                                | 24.6 ms: 1.02x faster                                                    |
| mako            | 10.1 ms                                                                | 9.93 ms: 1.01x faster                                                    |
| django_template | 33.0 ms                                                                | 33.4 ms: 1.01x slower                                                    |
| genshi_xml      | 57.1 ms                                                                | 59.1 ms: 1.03x slower                                                    |
| Geometric mean  | (ref)                                                                  | 1.00x slower                                                             |

All benchmarks:
===============

| Benchmark              | bm-20241120-linux-x86_64-python-0af4ec30bd2e3a523503-3.14.0a2+-0af4ec3 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_2048-3.14.0a2+-7b551b8 |
|------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_generate     | 83.0 ms                                                                | 78.5 ms: 1.06x faster                                                    |
| xml_etree_process      | 57.5 ms                                                                | 55.3 ms: 1.04x faster                                                    |
| pylint                 | 284 ms                                                                 | 275 ms: 1.04x faster                                                     |
| nqueens                | 90.8 ms                                                                | 87.9 ms: 1.03x faster                                                    |
| pyflate                | 452 ms                                                                 | 439 ms: 1.03x faster                                                     |
| meteor_contest         | 108 ms                                                                 | 105 ms: 1.02x faster                                                     |
| go                     | 134 ms                                                                 | 131 ms: 1.02x faster                                                     |
| connected_components   | 440 ms                                                                 | 431 ms: 1.02x faster                                                     |
| sympy_sum              | 160 ms                                                                 | 157 ms: 1.02x faster                                                     |
| sympy_str              | 287 ms                                                                 | 283 ms: 1.02x faster                                                     |
| shortest_path          | 485 ms                                                                 | 478 ms: 1.02x faster                                                     |
| genshi_text            | 25.0 ms                                                                | 24.6 ms: 1.02x faster                                                    |
| sympy_integrate        | 21.0 ms                                                                | 20.7 ms: 1.02x faster                                                    |
| regex_compile          | 131 ms                                                                 | 129 ms: 1.01x faster                                                     |
| mako                   | 10.1 ms                                                                | 9.93 ms: 1.01x faster                                                    |
| docutils               | 2.83 sec                                                               | 2.79 sec: 1.01x faster                                                   |
| many_optionals         | 990 us                                                                 | 977 us: 1.01x faster                                                     |
| pathlib                | 16.4 ms                                                                | 16.2 ms: 1.01x faster                                                    |
| json_dumps             | 11.2 ms                                                                | 11.1 ms: 1.01x faster                                                    |
| xml_etree_iterparse    | 101 ms                                                                 | 100 ms: 1.01x faster                                                     |
| dulwich_log            | 68.0 ms                                                                | 67.4 ms: 1.01x faster                                                    |
| sqlglot_transpile      | 1.65 ms                                                                | 1.63 ms: 1.01x faster                                                    |
| fannkuch               | 389 ms                                                                 | 385 ms: 1.01x faster                                                     |
| json                   | 4.85 ms                                                                | 4.80 ms: 1.01x faster                                                    |
| coroutines             | 23.4 ms                                                                | 23.2 ms: 1.01x faster                                                    |
| sqlalchemy_declarative | 131 ms                                                                 | 130 ms: 1.01x faster                                                     |
| pickle_pure_python     | 319 us                                                                 | 316 us: 1.01x faster                                                     |
| hexiom                 | 7.15 ms                                                                | 7.11 ms: 1.01x faster                                                    |
| sqlglot_normalize      | 111 ms                                                                 | 111 ms: 1.01x faster                                                     |
| sympy_expand           | 482 ms                                                                 | 480 ms: 1.00x faster                                                     |
| bench_thread_pool      | 876 us                                                                 | 873 us: 1.00x faster                                                     |
| async_generators       | 456 ms                                                                 | 455 ms: 1.00x faster                                                     |
| create_gc_cycles       | 2.64 ms                                                                | 2.64 ms: 1.00x faster                                                    |
| 2to3                   | 262 ms                                                                 | 261 ms: 1.00x faster                                                     |
| python_startup         | 12.8 ms                                                                | 12.8 ms: 1.00x faster                                                    |
| python_startup_no_site | 7.05 ms                                                                | 7.05 ms: 1.00x slower                                                    |
| sqlglot_optimize       | 55.5 ms                                                                | 55.7 ms: 1.00x slower                                                    |
| comprehensions         | 17.6 us                                                                | 17.7 us: 1.00x slower                                                    |
| coverage               | 83.8 ms                                                                | 84.2 ms: 1.01x slower                                                    |
| bpe_tokeniser          | 4.50 sec                                                               | 4.52 sec: 1.01x slower                                                   |
| bench_mp_pool          | 78.9 ms                                                                | 79.4 ms: 1.01x slower                                                    |
| chaos                  | 58.9 ms                                                                | 59.3 ms: 1.01x slower                                                    |
| crypto_pyaes           | 67.6 ms                                                                | 68.1 ms: 1.01x slower                                                    |
| regex_effbot           | 3.47 ms                                                                | 3.50 ms: 1.01x slower                                                    |
| deltablue              | 3.19 ms                                                                | 3.22 ms: 1.01x slower                                                    |
| tomli_loads            | 1.95 sec                                                               | 1.97 sec: 1.01x slower                                                   |
| logging_silent         | 99.4 ns                                                                | 100 ns: 1.01x slower                                                     |
| logging_simple         | 5.55 us                                                                | 5.61 us: 1.01x slower                                                    |
| regex_dna              | 223 ms                                                                 | 226 ms: 1.01x slower                                                     |
| django_template        | 33.0 ms                                                                | 33.4 ms: 1.01x slower                                                    |
| subparsers             | 21.0 ms                                                                | 21.2 ms: 1.01x slower                                                    |
| thrift                 | 776 us                                                                 | 785 us: 1.01x slower                                                     |
| pycparser              | 1.13 sec                                                               | 1.14 sec: 1.01x slower                                                   |
| raytrace               | 280 ms                                                                 | 285 ms: 1.02x slower                                                     |
| spectral_norm          | 112 ms                                                                 | 115 ms: 1.02x slower                                                     |
| regex_v8               | 25.5 ms                                                                | 26.0 ms: 1.02x slower                                                    |
| pidigits               | 186 ms                                                                 | 191 ms: 1.02x slower                                                     |
| gc_traversal           | 4.35 ms                                                                | 4.47 ms: 1.03x slower                                                    |
| genshi_xml             | 57.1 ms                                                                | 59.1 ms: 1.03x slower                                                    |
| pprint_pformat         | 1.46 sec                                                               | 1.51 sec: 1.04x slower                                                   |
| generators             | 35.2 ms                                                                | 37.1 ms: 1.05x slower                                                    |
| richards               | 36.9 ms                                                                | 39.4 ms: 1.07x slower                                                    |
| mdp                    | 2.59 sec                                                               | 2.78 sec: 1.07x slower                                                   |
| richards_super         | 42.5 ms                                                                | 45.8 ms: 1.08x slower                                                    |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                             |

Benchmark hidden because not significant (33): async_tree_cpu_io_mixed_tg, xml_etree_parse, k_core, sqlite_synth, djangocms, typing_runtime_protocols, async_tree_cpu_io_mixed, async_tree_none_tg, deepcopy, sphinx, scimark_sor, unpickle_pure_python, scimark_sparse_mat_mult, nbody, deepcopy_memo, scimark_monte_carlo, float, sqlglot_parse, scimark_lu, asyncio_websockets, html5lib, scimark_fft, async_tree_none, json_loads, logging_format, async_tree_io, deepcopy_reduce, async_tree_io_tg, async_tree_memoization_tg, sqlalchemy_imperative, telco, pprint_safe_repr, async_tree_memoization

- Geometric mean (including insignificant results): 1.001x slower
# HPT report

- Reliability score: 73.57% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x