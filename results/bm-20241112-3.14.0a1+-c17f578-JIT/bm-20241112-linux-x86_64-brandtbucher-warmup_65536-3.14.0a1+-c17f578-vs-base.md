# Results vs. base

- fork: brandtbucher
- ref: warmup_65536
- machine: linux-x86_64
- commit hash: c17f578
- commit date: 2024-11-12
- overall geometric mean: 1.013x faster
- HPT reliability: 96.25%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.96x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241112-linux-x86_64-brandtbucher-warmup_65536-3.14.0a1+-c17f578 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 280 ms                                                                 | 258 ms: 1.09x faster                                                 |
| docutils       | 2.95 sec                                                               | 2.81 sec: 1.05x faster                                               |
| html5lib       | 67.0 ms                                                                | 66.4 ms: 1.01x faster                                                |
| sphinx         | 1.18 sec                                                               | 1.10 sec: 1.07x faster                                               |
| Geometric mean | (ref)                                                                  | 1.05x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241112-linux-x86_64-brandtbucher-warmup_65536-3.14.0a1+-c17f578 |
|--------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| asyncio_websockets | 551 ms                                                                 | 553 ms: 1.00x slower                                                 |
| coroutines         | 23.2 ms                                                                | 23.4 ms: 1.00x slower                                                |
| async_generators   | 456 ms                                                                 | 462 ms: 1.01x slower                                                 |
| Geometric mean     | (ref)                                                                  | 1.00x slower                                                         |

Benchmark hidden because not significant (8): async_tree_memoization, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_none, async_tree_io_tg, async_tree_none_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241112-linux-x86_64-brandtbucher-warmup_65536-3.14.0a1+-c17f578 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| pidigits       | 187 ms                                                                 | 187 ms: 1.00x slower                                                 |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                         |

Benchmark hidden because not significant (2): nbody, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241112-linux-x86_64-brandtbucher-warmup_65536-3.14.0a1+-c17f578 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 140 ms                                                                 | 130 ms: 1.08x faster                                                 |
| regex_effbot   | 3.77 ms                                                                | 3.74 ms: 1.01x faster                                                |
| regex_dna      | 216 ms                                                                 | 219 ms: 1.01x slower                                                 |
| regex_v8       | 24.6 ms                                                                | 25.1 ms: 1.02x slower                                                |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241112-linux-x86_64-brandtbucher-warmup_65536-3.14.0a1+-c17f578 |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| unpickle_pure_python | 219 us                                                                 | 200 us: 1.09x faster                                                 |
| xml_etree_process    | 56.0 ms                                                                | 55.2 ms: 1.02x faster                                                |
| xml_etree_generate   | 79.6 ms                                                                | 78.7 ms: 1.01x faster                                                |
| pickle_pure_python   | 321 us                                                                 | 318 us: 1.01x faster                                                 |
| json_loads           | 26.8 us                                                                | 27.1 us: 1.01x slower                                                |
| xml_etree_iterparse  | 101 ms                                                                 | 103 ms: 1.03x slower                                                 |
| xml_etree_parse      | 148 ms                                                                 | 160 ms: 1.08x slower                                                 |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                         |

Benchmark hidden because not significant (2): tomli_loads, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241112-linux-x86_64-brandtbucher-warmup_65536-3.14.0a1+-c17f578 |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 7.14 ms                                                                | 7.09 ms: 1.01x faster                                                |
| python_startup         | 12.8 ms                                                                | 12.8 ms: 1.00x faster                                                |
| Geometric mean         | (ref)                                                                  | 1.01x faster                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241112-linux-x86_64-brandtbucher-warmup_65536-3.14.0a1+-c17f578 |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_xml      | 59.9 ms                                                                | 57.2 ms: 1.05x faster                                                |
| genshi_text     | 25.1 ms                                                                | 24.2 ms: 1.03x faster                                                |
| mako            | 10.3 ms                                                                | 10.2 ms: 1.01x faster                                                |
| django_template | 34.3 ms                                                                | 36.1 ms: 1.05x slower                                                |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                         |

All benchmarks:
===============

| Benchmark                | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241112-linux-x86_64-brandtbucher-warmup_65536-3.14.0a1+-c17f578 |
|--------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| pylint                   | 380 ms                                                                 | 327 ms: 1.16x faster                                                 |
| sympy_integrate          | 23.6 ms                                                                | 20.4 ms: 1.16x faster                                                |
| sqlalchemy_declarative   | 148 ms                                                                 | 129 ms: 1.15x faster                                                 |
| sympy_sum                | 176 ms                                                                 | 155 ms: 1.14x faster                                                 |
| sqlglot_optimize         | 60.3 ms                                                                | 54.2 ms: 1.11x faster                                                |
| sympy_str                | 305 ms                                                                 | 275 ms: 1.11x faster                                                 |
| unpickle_pure_python     | 219 us                                                                 | 200 us: 1.09x faster                                                 |
| sympy_expand             | 509 ms                                                                 | 467 ms: 1.09x faster                                                 |
| 2to3                     | 280 ms                                                                 | 258 ms: 1.09x faster                                                 |
| regex_compile            | 140 ms                                                                 | 130 ms: 1.08x faster                                                 |
| sphinx                   | 1.18 sec                                                               | 1.10 sec: 1.07x faster                                               |
| bench_mp_pool            | 84.8 ms                                                                | 79.2 ms: 1.07x faster                                                |
| sqlglot_transpile        | 1.69 ms                                                                | 1.59 ms: 1.06x faster                                                |
| hexiom                   | 7.08 ms                                                                | 6.71 ms: 1.06x faster                                                |
| docutils                 | 2.95 sec                                                               | 2.81 sec: 1.05x faster                                               |
| go                       | 133 ms                                                                 | 127 ms: 1.05x faster                                                 |
| genshi_xml               | 59.9 ms                                                                | 57.2 ms: 1.05x faster                                                |
| sqlglot_normalize        | 114 ms                                                                 | 110 ms: 1.04x faster                                                 |
| deltablue                | 3.31 ms                                                                | 3.19 ms: 1.04x faster                                                |
| pprint_pformat           | 1.51 sec                                                               | 1.46 sec: 1.04x faster                                               |
| raytrace                 | 283 ms                                                                 | 273 ms: 1.04x faster                                                 |
| genshi_text              | 25.1 ms                                                                | 24.2 ms: 1.03x faster                                                |
| logging_silent           | 102 ns                                                                 | 98.7 ns: 1.03x faster                                                |
| dulwich_log              | 67.7 ms                                                                | 65.7 ms: 1.03x faster                                                |
| sqlglot_parse            | 1.33 ms                                                                | 1.29 ms: 1.03x faster                                                |
| mdp                      | 2.62 sec                                                               | 2.55 sec: 1.03x faster                                               |
| bench_thread_pool        | 889 us                                                                 | 869 us: 1.02x faster                                                 |
| sqlalchemy_imperative    | 17.8 ms                                                                | 17.5 ms: 1.02x faster                                                |
| xml_etree_process        | 56.0 ms                                                                | 55.2 ms: 1.02x faster                                                |
| pprint_safe_repr         | 724 ms                                                                 | 715 ms: 1.01x faster                                                 |
| typing_runtime_protocols | 170 us                                                                 | 168 us: 1.01x faster                                                 |
| xml_etree_generate       | 79.6 ms                                                                | 78.7 ms: 1.01x faster                                                |
| fannkuch                 | 389 ms                                                                 | 385 ms: 1.01x faster                                                 |
| html5lib                 | 67.0 ms                                                                | 66.4 ms: 1.01x faster                                                |
| comprehensions           | 17.5 us                                                                | 17.4 us: 1.01x faster                                                |
| coverage                 | 84.9 ms                                                                | 84.1 ms: 1.01x faster                                                |
| mako                     | 10.3 ms                                                                | 10.2 ms: 1.01x faster                                                |
| pickle_pure_python       | 321 us                                                                 | 318 us: 1.01x faster                                                 |
| regex_effbot             | 3.77 ms                                                                | 3.74 ms: 1.01x faster                                                |
| generators               | 36.6 ms                                                                | 36.4 ms: 1.01x faster                                                |
| deepcopy_memo            | 29.6 us                                                                | 29.4 us: 1.01x faster                                                |
| python_startup_no_site   | 7.14 ms                                                                | 7.09 ms: 1.01x faster                                                |
| bpe_tokeniser            | 4.53 sec                                                               | 4.50 sec: 1.01x faster                                               |
| python_startup           | 12.8 ms                                                                | 12.8 ms: 1.00x faster                                                |
| create_gc_cycles         | 2.71 ms                                                                | 2.70 ms: 1.00x faster                                                |
| pidigits                 | 187 ms                                                                 | 187 ms: 1.00x slower                                                 |
| connected_components     | 437 ms                                                                 | 438 ms: 1.00x slower                                                 |
| asyncio_websockets       | 551 ms                                                                 | 553 ms: 1.00x slower                                                 |
| coroutines               | 23.2 ms                                                                | 23.4 ms: 1.00x slower                                                |
| scimark_monte_carlo      | 64.8 ms                                                                | 65.2 ms: 1.01x slower                                                |
| crypto_pyaes             | 68.5 ms                                                                | 69.0 ms: 1.01x slower                                                |
| json_loads               | 26.8 us                                                                | 27.1 us: 1.01x slower                                                |
| scimark_sor              | 119 ms                                                                 | 120 ms: 1.01x slower                                                 |
| regex_dna                | 216 ms                                                                 | 219 ms: 1.01x slower                                                 |
| thrift                   | 779 us                                                                 | 788 us: 1.01x slower                                                 |
| meteor_contest           | 109 ms                                                                 | 111 ms: 1.01x slower                                                 |
| async_generators         | 456 ms                                                                 | 462 ms: 1.01x slower                                                 |
| gc_traversal             | 4.74 ms                                                                | 4.80 ms: 1.01x slower                                                |
| chaos                    | 59.1 ms                                                                | 60.0 ms: 1.01x slower                                                |
| deepcopy                 | 267 us                                                                 | 272 us: 1.02x slower                                                 |
| telco                    | 7.67 ms                                                                | 7.80 ms: 1.02x slower                                                |
| logging_format           | 6.17 us                                                                | 6.30 us: 1.02x slower                                                |
| regex_v8                 | 24.6 ms                                                                | 25.1 ms: 1.02x slower                                                |
| scimark_fft              | 318 ms                                                                 | 326 ms: 1.02x slower                                                 |
| pycparser                | 1.16 sec                                                               | 1.19 sec: 1.03x slower                                               |
| xml_etree_iterparse      | 101 ms                                                                 | 103 ms: 1.03x slower                                                 |
| logging_simple           | 5.56 us                                                                | 5.72 us: 1.03x slower                                                |
| nqueens                  | 87.9 ms                                                                | 90.5 ms: 1.03x slower                                                |
| deepcopy_reduce          | 2.66 us                                                                | 2.75 us: 1.03x slower                                                |
| pyflate                  | 449 ms                                                                 | 464 ms: 1.03x slower                                                 |
| spectral_norm            | 115 ms                                                                 | 120 ms: 1.04x slower                                                 |
| django_template          | 34.3 ms                                                                | 36.1 ms: 1.05x slower                                                |
| xml_etree_parse          | 148 ms                                                                 | 160 ms: 1.08x slower                                                 |
| richards                 | 40.7 ms                                                                | 45.2 ms: 1.11x slower                                                |
| richards_super           | 47.1 ms                                                                | 52.4 ms: 1.11x slower                                                |
| Geometric mean           | (ref)                                                                  | 1.01x faster                                                         |

Benchmark hidden because not significant (19): tomli_loads, async_tree_memoization, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, scimark_lu, json, json_dumps, async_tree_cpu_io_mixed, async_tree_none, pathlib, shortest_path, scimark_sparse_mat_mult, async_tree_io_tg, nbody, sqlite_synth, float, k_core, async_tree_none_tg, async_tree_io
Ignored benchmarks (3) of results/bm-20241107-3.14.0a1+-09d6f5d-JIT/bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d.json: djangocms, many_optionals, subparsers

- Geometric mean (including insignificant results): 1.013x faster
# HPT report

- Reliability score: 96.25% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.96x