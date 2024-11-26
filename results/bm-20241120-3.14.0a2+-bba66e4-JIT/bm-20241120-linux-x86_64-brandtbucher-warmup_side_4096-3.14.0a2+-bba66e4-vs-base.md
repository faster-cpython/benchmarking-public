# Results vs. base

- fork: brandtbucher
- ref: warmup_side_4096
- machine: linux-x86_64
- commit hash: bba66e4
- commit date: 2024-11-20
- overall geometric mean: 1.004x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241120-linux-x86_64-python-0af4ec30bd2e3a523503-3.14.0a2+-0af4ec3 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-bba66e4 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 262 ms                                                                 | 259 ms: 1.01x faster                                                     |
| docutils       | 2.83 sec                                                               | 2.77 sec: 1.02x faster                                                   |
| html5lib       | 66.8 ms                                                                | 66.3 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                             |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20241120-linux-x86_64-python-0af4ec30bd2e3a523503-3.14.0a2+-0af4ec3 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-bba66e4 |
|------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| coroutines       | 23.4 ms                                                                | 22.7 ms: 1.03x faster                                                    |
| async_generators | 456 ms                                                                 | 450 ms: 1.01x faster                                                     |
| Geometric mean   | (ref)                                                                  | 1.01x faster                                                             |

Benchmark hidden because not significant (9): async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_io, async_tree_io_tg, async_tree_none_tg, async_tree_memoization_tg, async_tree_none, asyncio_websockets, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241120-linux-x86_64-python-0af4ec30bd2e3a523503-3.14.0a2+-0af4ec3 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-bba66e4 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                                 | 186 ms: 1.00x faster                                                     |
| nbody          | 82.5 ms                                                                | 83.2 ms: 1.01x slower                                                    |
| float          | 77.8 ms                                                                | 79.0 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241120-linux-x86_64-python-0af4ec30bd2e3a523503-3.14.0a2+-0af4ec3 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-bba66e4 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_dna      | 223 ms                                                                 | 219 ms: 1.02x faster                                                     |
| regex_compile  | 131 ms                                                                 | 129 ms: 1.02x faster                                                     |
| regex_effbot   | 3.47 ms                                                                | 3.42 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                             |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241120-linux-x86_64-python-0af4ec30bd2e3a523503-3.14.0a2+-0af4ec3 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-bba66e4 |
|----------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_generate   | 83.0 ms                                                                | 79.0 ms: 1.05x faster                                                    |
| xml_etree_process    | 57.5 ms                                                                | 55.7 ms: 1.03x faster                                                    |
| json_dumps           | 11.2 ms                                                                | 11.1 ms: 1.01x faster                                                    |
| pickle_pure_python   | 319 us                                                                 | 317 us: 1.01x faster                                                     |
| json_loads           | 26.3 us                                                                | 26.1 us: 1.01x faster                                                    |
| unpickle_pure_python | 193 us                                                                 | 195 us: 1.01x slower                                                     |
| Geometric mean       | (ref)                                                                  | 1.01x faster                                                             |

Benchmark hidden because not significant (3): xml_etree_parse, xml_etree_iterparse, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241120-linux-x86_64-python-0af4ec30bd2e3a523503-3.14.0a2+-0af4ec3 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-bba66e4 |
|------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 12.8 ms                                                                | 12.8 ms: 1.00x faster                                                    |
| python_startup_no_site | 7.05 ms                                                                | 7.04 ms: 1.00x faster                                                    |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241120-linux-x86_64-python-0af4ec30bd2e3a523503-3.14.0a2+-0af4ec3 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-bba66e4 |
|-----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 10.1 ms                                                                | 10.0 ms: 1.00x faster                                                    |
| genshi_text     | 25.0 ms                                                                | 25.1 ms: 1.01x slower                                                    |
| django_template | 33.0 ms                                                                | 33.3 ms: 1.01x slower                                                    |
| genshi_xml      | 57.1 ms                                                                | 58.5 ms: 1.02x slower                                                    |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                             |

All benchmarks:
===============

| Benchmark               | bm-20241120-linux-x86_64-python-0af4ec30bd2e3a523503-3.14.0a2+-0af4ec3 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-bba66e4 |
|-------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_generate      | 83.0 ms                                                                | 79.0 ms: 1.05x faster                                                    |
| pylint                  | 284 ms                                                                 | 271 ms: 1.05x faster                                                     |
| scimark_sparse_mat_mult | 4.67 ms                                                                | 4.52 ms: 1.03x faster                                                    |
| xml_etree_process       | 57.5 ms                                                                | 55.7 ms: 1.03x faster                                                    |
| coroutines              | 23.4 ms                                                                | 22.7 ms: 1.03x faster                                                    |
| pyflate                 | 452 ms                                                                 | 438 ms: 1.03x faster                                                     |
| sympy_sum               | 160 ms                                                                 | 155 ms: 1.03x faster                                                     |
| nqueens                 | 90.8 ms                                                                | 88.5 ms: 1.03x faster                                                    |
| sympy_str               | 287 ms                                                                 | 280 ms: 1.03x faster                                                     |
| many_optionals          | 990 us                                                                 | 968 us: 1.02x faster                                                     |
| docutils                | 2.83 sec                                                               | 2.77 sec: 1.02x faster                                                   |
| hexiom                  | 7.15 ms                                                                | 7.02 ms: 1.02x faster                                                    |
| regex_dna               | 223 ms                                                                 | 219 ms: 1.02x faster                                                     |
| regex_compile           | 131 ms                                                                 | 129 ms: 1.02x faster                                                     |
| sympy_integrate         | 21.0 ms                                                                | 20.7 ms: 1.02x faster                                                    |
| regex_effbot            | 3.47 ms                                                                | 3.42 ms: 1.02x faster                                                    |
| json                    | 4.85 ms                                                                | 4.77 ms: 1.02x faster                                                    |
| dulwich_log             | 68.0 ms                                                                | 67.1 ms: 1.01x faster                                                    |
| sympy_expand            | 482 ms                                                                 | 475 ms: 1.01x faster                                                     |
| scimark_fft             | 317 ms                                                                 | 313 ms: 1.01x faster                                                     |
| sqlalchemy_imperative   | 17.2 ms                                                                | 17.0 ms: 1.01x faster                                                    |
| async_generators        | 456 ms                                                                 | 450 ms: 1.01x faster                                                     |
| scimark_lu              | 115 ms                                                                 | 114 ms: 1.01x faster                                                     |
| sqlglot_transpile       | 1.65 ms                                                                | 1.63 ms: 1.01x faster                                                    |
| sqlglot_parse           | 1.33 ms                                                                | 1.32 ms: 1.01x faster                                                    |
| sqlalchemy_declarative  | 131 ms                                                                 | 129 ms: 1.01x faster                                                     |
| connected_components    | 440 ms                                                                 | 435 ms: 1.01x faster                                                     |
| telco                   | 7.58 ms                                                                | 7.50 ms: 1.01x faster                                                    |
| sqlglot_normalize       | 111 ms                                                                 | 110 ms: 1.01x faster                                                     |
| shortest_path           | 485 ms                                                                 | 481 ms: 1.01x faster                                                     |
| 2to3                    | 262 ms                                                                 | 259 ms: 1.01x faster                                                     |
| logging_silent          | 99.4 ns                                                                | 98.5 ns: 1.01x faster                                                    |
| deepcopy_reduce         | 2.69 us                                                                | 2.67 us: 1.01x faster                                                    |
| meteor_contest          | 108 ms                                                                 | 107 ms: 1.01x faster                                                     |
| html5lib                | 66.8 ms                                                                | 66.3 ms: 1.01x faster                                                    |
| coverage                | 83.8 ms                                                                | 83.1 ms: 1.01x faster                                                    |
| json_dumps              | 11.2 ms                                                                | 11.1 ms: 1.01x faster                                                    |
| comprehensions          | 17.6 us                                                                | 17.5 us: 1.01x faster                                                    |
| crypto_pyaes            | 67.6 ms                                                                | 67.2 ms: 1.01x faster                                                    |
| pickle_pure_python      | 319 us                                                                 | 317 us: 1.01x faster                                                     |
| json_loads              | 26.3 us                                                                | 26.1 us: 1.01x faster                                                    |
| deepcopy                | 268 us                                                                 | 266 us: 1.01x faster                                                     |
| pathlib                 | 16.4 ms                                                                | 16.3 ms: 1.00x faster                                                    |
| bench_thread_pool       | 876 us                                                                 | 872 us: 1.00x faster                                                     |
| mako                    | 10.1 ms                                                                | 10.0 ms: 1.00x faster                                                    |
| python_startup          | 12.8 ms                                                                | 12.8 ms: 1.00x faster                                                    |
| pidigits                | 186 ms                                                                 | 186 ms: 1.00x faster                                                     |
| python_startup_no_site  | 7.05 ms                                                                | 7.04 ms: 1.00x faster                                                    |
| create_gc_cycles        | 2.64 ms                                                                | 2.65 ms: 1.00x slower                                                    |
| subparsers              | 21.0 ms                                                                | 21.1 ms: 1.00x slower                                                    |
| genshi_text             | 25.0 ms                                                                | 25.1 ms: 1.01x slower                                                    |
| logging_simple          | 5.55 us                                                                | 5.59 us: 1.01x slower                                                    |
| django_template         | 33.0 ms                                                                | 33.3 ms: 1.01x slower                                                    |
| chaos                   | 58.9 ms                                                                | 59.3 ms: 1.01x slower                                                    |
| nbody                   | 82.5 ms                                                                | 83.2 ms: 1.01x slower                                                    |
| pprint_pformat          | 1.46 sec                                                               | 1.47 sec: 1.01x slower                                                   |
| unpickle_pure_python    | 193 us                                                                 | 195 us: 1.01x slower                                                     |
| spectral_norm           | 112 ms                                                                 | 114 ms: 1.01x slower                                                     |
| float                   | 77.8 ms                                                                | 79.0 ms: 1.02x slower                                                    |
| raytrace                | 280 ms                                                                 | 285 ms: 1.02x slower                                                     |
| genshi_xml              | 57.1 ms                                                                | 58.5 ms: 1.02x slower                                                    |
| generators              | 35.2 ms                                                                | 36.5 ms: 1.04x slower                                                    |
| gc_traversal            | 4.35 ms                                                                | 4.54 ms: 1.04x slower                                                    |
| pycparser               | 1.13 sec                                                               | 1.18 sec: 1.05x slower                                                   |
| richards                | 36.9 ms                                                                | 38.7 ms: 1.05x slower                                                    |
| richards_super          | 42.5 ms                                                                | 44.7 ms: 1.05x slower                                                    |
| Geometric mean          | (ref)                                                                  | 1.00x faster                                                             |

Benchmark hidden because not significant (31): djangocms, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, sphinx, async_tree_io, async_tree_io_tg, typing_runtime_protocols, pprint_safe_repr, async_tree_none_tg, xml_etree_parse, thrift, async_tree_memoization_tg, async_tree_none, deepcopy_memo, go, bench_mp_pool, scimark_sor, xml_etree_iterparse, deltablue, bpe_tokeniser, mdp, asyncio_websockets, sqlglot_optimize, regex_v8, fannkuch, k_core, async_tree_memoization, sqlite_synth, tomli_loads, logging_format, scimark_monte_carlo

- Geometric mean (including insignificant results): 1.004x faster
# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x