# Results vs. base

- fork: brandtbucher
- ref: warmup_16384
- machine: linux-x86_64
- commit hash: 1723e00
- commit date: 2024-11-11
- overall geometric mean: 1.015x faster
- HPT reliability: 98.73%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.96x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241111-linux-x86_64-brandtbucher-warmup_16384-3.14.0a1+-1723e00 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 280 ms                                                                 | 256 ms: 1.10x faster                                                 |
| docutils       | 2.95 sec                                                               | 2.86 sec: 1.03x faster                                               |
| html5lib       | 67.0 ms                                                                | 66.5 ms: 1.01x faster                                                |
| sphinx         | 1.18 sec                                                               | 1.12 sec: 1.05x faster                                               |
| Geometric mean | (ref)                                                                  | 1.05x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241111-linux-x86_64-brandtbucher-warmup_16384-3.14.0a1+-1723e00 |
|--------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| asyncio_websockets | 551 ms                                                                 | 553 ms: 1.00x slower                                                 |
| coroutines         | 23.2 ms                                                                | 23.4 ms: 1.01x slower                                                |
| async_generators   | 456 ms                                                                 | 460 ms: 1.01x slower                                                 |
| Geometric mean     | (ref)                                                                  | 1.01x slower                                                         |

Benchmark hidden because not significant (8): async_tree_memoization_tg, async_tree_memoization, async_tree_io, async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_none, async_tree_cpu_io_mixed, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241111-linux-x86_64-brandtbucher-warmup_16384-3.14.0a1+-1723e00 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 76.7 ms                                                                | 77.1 ms: 1.00x slower                                                |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                         |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241111-linux-x86_64-brandtbucher-warmup_16384-3.14.0a1+-1723e00 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 140 ms                                                                 | 131 ms: 1.07x faster                                                 |
| regex_dna      | 216 ms                                                                 | 211 ms: 1.02x faster                                                 |
| regex_effbot   | 3.77 ms                                                                | 3.68 ms: 1.02x faster                                                |
| regex_v8       | 24.6 ms                                                                | 25.0 ms: 1.02x slower                                                |
| Geometric mean | (ref)                                                                  | 1.03x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241111-linux-x86_64-brandtbucher-warmup_16384-3.14.0a1+-1723e00 |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| unpickle_pure_python | 219 us                                                                 | 194 us: 1.13x faster                                                 |
| xml_etree_process    | 56.0 ms                                                                | 55.6 ms: 1.01x faster                                                |
| json_loads           | 26.8 us                                                                | 26.7 us: 1.00x faster                                                |
| pickle_pure_python   | 321 us                                                                 | 324 us: 1.01x slower                                                 |
| xml_etree_iterparse  | 101 ms                                                                 | 102 ms: 1.02x slower                                                 |
| xml_etree_parse      | 148 ms                                                                 | 156 ms: 1.05x slower                                                 |
| Geometric mean       | (ref)                                                                  | 1.01x faster                                                         |

Benchmark hidden because not significant (3): tomli_loads, xml_etree_generate, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241111-linux-x86_64-brandtbucher-warmup_16384-3.14.0a1+-1723e00 |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 7.14 ms                                                                | 7.05 ms: 1.01x faster                                                |
| python_startup         | 12.8 ms                                                                | 12.7 ms: 1.01x faster                                                |
| Geometric mean         | (ref)                                                                  | 1.01x faster                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241111-linux-x86_64-brandtbucher-warmup_16384-3.14.0a1+-1723e00 |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_xml      | 59.9 ms                                                                | 56.9 ms: 1.05x faster                                                |
| genshi_text     | 25.1 ms                                                                | 24.3 ms: 1.03x faster                                                |
| django_template | 34.3 ms                                                                | 36.4 ms: 1.06x slower                                                |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                         |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241111-linux-x86_64-brandtbucher-warmup_16384-3.14.0a1+-1723e00 |
|--------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| pylint                   | 380 ms                                                                 | 333 ms: 1.14x faster                                                 |
| sympy_integrate          | 23.6 ms                                                                | 20.7 ms: 1.14x faster                                                |
| sqlalchemy_declarative   | 148 ms                                                                 | 130 ms: 1.14x faster                                                 |
| unpickle_pure_python     | 219 us                                                                 | 194 us: 1.13x faster                                                 |
| sympy_sum                | 176 ms                                                                 | 157 ms: 1.12x faster                                                 |
| 2to3                     | 280 ms                                                                 | 256 ms: 1.10x faster                                                 |
| sqlglot_optimize         | 60.3 ms                                                                | 55.5 ms: 1.09x faster                                                |
| sympy_str                | 305 ms                                                                 | 281 ms: 1.08x faster                                                 |
| bench_mp_pool            | 84.8 ms                                                                | 78.3 ms: 1.08x faster                                                |
| regex_compile            | 140 ms                                                                 | 131 ms: 1.07x faster                                                 |
| genshi_xml               | 59.9 ms                                                                | 56.9 ms: 1.05x faster                                                |
| sphinx                   | 1.18 sec                                                               | 1.12 sec: 1.05x faster                                               |
| gc_traversal             | 4.74 ms                                                                | 4.52 ms: 1.05x faster                                                |
| sqlalchemy_imperative    | 17.8 ms                                                                | 17.1 ms: 1.04x faster                                                |
| sqlglot_transpile        | 1.69 ms                                                                | 1.63 ms: 1.04x faster                                                |
| go                       | 133 ms                                                                 | 128 ms: 1.04x faster                                                 |
| dulwich_log              | 67.7 ms                                                                | 65.6 ms: 1.03x faster                                                |
| genshi_text              | 25.1 ms                                                                | 24.3 ms: 1.03x faster                                                |
| docutils                 | 2.95 sec                                                               | 2.86 sec: 1.03x faster                                               |
| pycparser                | 1.16 sec                                                               | 1.13 sec: 1.03x faster                                               |
| sqlglot_normalize        | 114 ms                                                                 | 111 ms: 1.03x faster                                                 |
| comprehensions           | 17.5 us                                                                | 17.1 us: 1.02x faster                                                |
| regex_dna                | 216 ms                                                                 | 211 ms: 1.02x faster                                                 |
| regex_effbot             | 3.77 ms                                                                | 3.68 ms: 1.02x faster                                                |
| logging_silent           | 102 ns                                                                 | 99.5 ns: 1.02x faster                                                |
| generators               | 36.6 ms                                                                | 35.8 ms: 1.02x faster                                                |
| sympy_expand             | 509 ms                                                                 | 498 ms: 1.02x faster                                                 |
| create_gc_cycles         | 2.71 ms                                                                | 2.66 ms: 1.02x faster                                                |
| json                     | 4.98 ms                                                                | 4.90 ms: 1.02x faster                                                |
| hexiom                   | 7.08 ms                                                                | 6.98 ms: 1.01x faster                                                |
| deltablue                | 3.31 ms                                                                | 3.27 ms: 1.01x faster                                                |
| bench_thread_pool        | 889 us                                                                 | 876 us: 1.01x faster                                                 |
| python_startup_no_site   | 7.14 ms                                                                | 7.05 ms: 1.01x faster                                                |
| python_startup           | 12.8 ms                                                                | 12.7 ms: 1.01x faster                                                |
| mdp                      | 2.62 sec                                                               | 2.59 sec: 1.01x faster                                               |
| raytrace                 | 283 ms                                                                 | 280 ms: 1.01x faster                                                 |
| fannkuch                 | 389 ms                                                                 | 385 ms: 1.01x faster                                                 |
| meteor_contest           | 109 ms                                                                 | 108 ms: 1.01x faster                                                 |
| crypto_pyaes             | 68.5 ms                                                                | 67.8 ms: 1.01x faster                                                |
| typing_runtime_protocols | 170 us                                                                 | 168 us: 1.01x faster                                                 |
| html5lib                 | 67.0 ms                                                                | 66.5 ms: 1.01x faster                                                |
| shortest_path            | 482 ms                                                                 | 478 ms: 1.01x faster                                                 |
| xml_etree_process        | 56.0 ms                                                                | 55.6 ms: 1.01x faster                                                |
| bpe_tokeniser            | 4.53 sec                                                               | 4.49 sec: 1.01x faster                                               |
| spectral_norm            | 115 ms                                                                 | 114 ms: 1.01x faster                                                 |
| pathlib                  | 16.1 ms                                                                | 16.0 ms: 1.01x faster                                                |
| json_loads               | 26.8 us                                                                | 26.7 us: 1.00x faster                                                |
| sqlite_synth             | 2.80 us                                                                | 2.79 us: 1.00x faster                                                |
| asyncio_websockets       | 551 ms                                                                 | 553 ms: 1.00x slower                                                 |
| float                    | 76.7 ms                                                                | 77.1 ms: 1.00x slower                                                |
| coroutines               | 23.2 ms                                                                | 23.4 ms: 1.01x slower                                                |
| logging_simple           | 5.56 us                                                                | 5.61 us: 1.01x slower                                                |
| pickle_pure_python       | 321 us                                                                 | 324 us: 1.01x slower                                                 |
| async_generators         | 456 ms                                                                 | 460 ms: 1.01x slower                                                 |
| nqueens                  | 87.9 ms                                                                | 89.2 ms: 1.02x slower                                                |
| coverage                 | 84.9 ms                                                                | 86.2 ms: 1.02x slower                                                |
| regex_v8                 | 24.6 ms                                                                | 25.0 ms: 1.02x slower                                                |
| chaos                    | 59.1 ms                                                                | 60.1 ms: 1.02x slower                                                |
| scimark_sparse_mat_mult  | 4.62 ms                                                                | 4.70 ms: 1.02x slower                                                |
| scimark_fft              | 318 ms                                                                 | 323 ms: 1.02x slower                                                 |
| xml_etree_iterparse      | 101 ms                                                                 | 102 ms: 1.02x slower                                                 |
| scimark_sor              | 119 ms                                                                 | 121 ms: 1.02x slower                                                 |
| deepcopy                 | 267 us                                                                 | 273 us: 1.02x slower                                                 |
| pprint_pformat           | 1.51 sec                                                               | 1.55 sec: 1.02x slower                                               |
| deepcopy_memo            | 29.6 us                                                                | 30.3 us: 1.02x slower                                                |
| scimark_lu               | 113 ms                                                                 | 116 ms: 1.02x slower                                                 |
| richards_super           | 47.1 ms                                                                | 48.4 ms: 1.03x slower                                                |
| pprint_safe_repr         | 724 ms                                                                 | 749 ms: 1.03x slower                                                 |
| xml_etree_parse          | 148 ms                                                                 | 156 ms: 1.05x slower                                                 |
| django_template          | 34.3 ms                                                                | 36.4 ms: 1.06x slower                                                |
| deepcopy_reduce          | 2.66 us                                                                | 2.83 us: 1.06x slower                                                |
| Geometric mean           | (ref)                                                                  | 1.01x faster                                                         |

Benchmark hidden because not significant (23): tomli_loads, mako, logging_format, scimark_monte_carlo, xml_etree_generate, k_core, async_tree_memoization_tg, pidigits, connected_components, async_tree_memoization, thrift, pyflate, nbody, sqlglot_parse, async_tree_io, async_tree_io_tg, async_tree_cpu_io_mixed_tg, telco, async_tree_none, json_dumps, async_tree_cpu_io_mixed, async_tree_none_tg, richards
Ignored benchmarks (3) of results/bm-20241107-3.14.0a1+-09d6f5d-JIT/bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d.json: djangocms, many_optionals, subparsers

- Geometric mean (including insignificant results): 1.015x faster
# HPT report

- Reliability score: 98.73% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.96x