# Results vs. base

- fork: brandtbucher
- ref: warmup_32768
- machine: linux-x86_64
- commit hash: c561277
- commit date: 2024-11-12
- overall geometric mean: 1.014x faster
- HPT reliability: 83.84%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.96x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241112-linux-x86_64-brandtbucher-warmup_32768-3.14.0a1+-c561277 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 280 ms                                                                 | 256 ms: 1.09x faster                                                 |
| docutils       | 2.95 sec                                                               | 2.83 sec: 1.04x faster                                               |
| html5lib       | 67.0 ms                                                                | 66.5 ms: 1.01x faster                                                |
| sphinx         | 1.18 sec                                                               | 1.10 sec: 1.07x faster                                               |
| Geometric mean | (ref)                                                                  | 1.05x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241112-linux-x86_64-brandtbucher-warmup_32768-3.14.0a1+-c561277 |
|------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| coroutines       | 23.2 ms                                                                | 23.0 ms: 1.01x faster                                                |
| async_tree_io_tg | 978 ms                                                                 | 986 ms: 1.01x slower                                                 |
| async_generators | 456 ms                                                                 | 461 ms: 1.01x slower                                                 |
| Geometric mean   | (ref)                                                                  | 1.00x slower                                                         |

Benchmark hidden because not significant (8): async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed, asyncio_websockets, async_tree_io, async_tree_none, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241112-linux-x86_64-brandtbucher-warmup_32768-3.14.0a1+-c561277 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| pidigits       | 187 ms                                                                 | 187 ms: 1.00x slower                                                 |
| nbody          | 82.3 ms                                                                | 84.5 ms: 1.03x slower                                                |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                         |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241112-linux-x86_64-brandtbucher-warmup_32768-3.14.0a1+-c561277 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 140 ms                                                                 | 130 ms: 1.08x faster                                                 |
| regex_effbot   | 3.77 ms                                                                | 3.58 ms: 1.05x faster                                                |
| regex_dna      | 216 ms                                                                 | 215 ms: 1.00x faster                                                 |
| regex_v8       | 24.6 ms                                                                | 25.1 ms: 1.02x slower                                                |
| Geometric mean | (ref)                                                                  | 1.03x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241112-linux-x86_64-brandtbucher-warmup_32768-3.14.0a1+-c561277 |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| unpickle_pure_python | 219 us                                                                 | 199 us: 1.10x faster                                                 |
| tomli_loads          | 2.00 sec                                                               | 1.96 sec: 1.02x faster                                               |
| xml_etree_generate   | 79.6 ms                                                                | 78.1 ms: 1.02x faster                                                |
| pickle_pure_python   | 321 us                                                                 | 326 us: 1.01x slower                                                 |
| xml_etree_iterparse  | 101 ms                                                                 | 102 ms: 1.02x slower                                                 |
| xml_etree_parse      | 148 ms                                                                 | 155 ms: 1.04x slower                                                 |
| Geometric mean       | (ref)                                                                  | 1.01x faster                                                         |

Benchmark hidden because not significant (3): xml_etree_process, json_loads, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241112-linux-x86_64-brandtbucher-warmup_32768-3.14.0a1+-c561277 |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 12.8 ms                                                                | 12.7 ms: 1.01x faster                                                |
| python_startup_no_site | 7.14 ms                                                                | 7.05 ms: 1.01x faster                                                |
| Geometric mean         | (ref)                                                                  | 1.01x faster                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241112-linux-x86_64-brandtbucher-warmup_32768-3.14.0a1+-c561277 |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_text     | 25.1 ms                                                                | 23.7 ms: 1.06x faster                                                |
| genshi_xml      | 59.9 ms                                                                | 56.9 ms: 1.05x faster                                                |
| mako            | 10.3 ms                                                                | 10.2 ms: 1.00x faster                                                |
| django_template | 34.3 ms                                                                | 36.3 ms: 1.06x slower                                                |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                         |

All benchmarks:
===============

| Benchmark                | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241112-linux-x86_64-brandtbucher-warmup_32768-3.14.0a1+-c561277 |
|--------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| sympy_integrate          | 23.6 ms                                                                | 20.3 ms: 1.16x faster                                                |
| pylint                   | 380 ms                                                                 | 329 ms: 1.16x faster                                                 |
| sqlalchemy_declarative   | 148 ms                                                                 | 129 ms: 1.14x faster                                                 |
| sympy_sum                | 176 ms                                                                 | 155 ms: 1.13x faster                                                 |
| sqlglot_optimize         | 60.3 ms                                                                | 54.3 ms: 1.11x faster                                                |
| unpickle_pure_python     | 219 us                                                                 | 199 us: 1.10x faster                                                 |
| sympy_str                | 305 ms                                                                 | 278 ms: 1.10x faster                                                 |
| 2to3                     | 280 ms                                                                 | 256 ms: 1.09x faster                                                 |
| bench_mp_pool            | 84.8 ms                                                                | 78.4 ms: 1.08x faster                                                |
| regex_compile            | 140 ms                                                                 | 130 ms: 1.08x faster                                                 |
| sphinx                   | 1.18 sec                                                               | 1.10 sec: 1.07x faster                                               |
| hexiom                   | 7.08 ms                                                                | 6.68 ms: 1.06x faster                                                |
| sqlglot_transpile        | 1.69 ms                                                                | 1.59 ms: 1.06x faster                                                |
| genshi_text              | 25.1 ms                                                                | 23.7 ms: 1.06x faster                                                |
| regex_effbot             | 3.77 ms                                                                | 3.58 ms: 1.05x faster                                                |
| dulwich_log              | 67.7 ms                                                                | 64.3 ms: 1.05x faster                                                |
| sympy_expand             | 509 ms                                                                 | 483 ms: 1.05x faster                                                 |
| genshi_xml               | 59.9 ms                                                                | 56.9 ms: 1.05x faster                                                |
| sqlalchemy_imperative    | 17.8 ms                                                                | 16.9 ms: 1.05x faster                                                |
| sqlglot_normalize        | 114 ms                                                                 | 109 ms: 1.05x faster                                                 |
| gc_traversal             | 4.74 ms                                                                | 4.52 ms: 1.05x faster                                                |
| deltablue                | 3.31 ms                                                                | 3.17 ms: 1.05x faster                                                |
| docutils                 | 2.95 sec                                                               | 2.83 sec: 1.04x faster                                               |
| go                       | 133 ms                                                                 | 129 ms: 1.04x faster                                                 |
| tomli_loads              | 2.00 sec                                                               | 1.96 sec: 1.02x faster                                               |
| xml_etree_generate       | 79.6 ms                                                                | 78.1 ms: 1.02x faster                                                |
| json                     | 4.98 ms                                                                | 4.88 ms: 1.02x faster                                                |
| bench_thread_pool        | 889 us                                                                 | 873 us: 1.02x faster                                                 |
| scimark_sparse_mat_mult  | 4.62 ms                                                                | 4.54 ms: 1.02x faster                                                |
| raytrace                 | 283 ms                                                                 | 278 ms: 1.02x faster                                                 |
| generators               | 36.6 ms                                                                | 36.0 ms: 1.02x faster                                                |
| create_gc_cycles         | 2.71 ms                                                                | 2.67 ms: 1.02x faster                                                |
| typing_runtime_protocols | 170 us                                                                 | 167 us: 1.01x faster                                                 |
| python_startup           | 12.8 ms                                                                | 12.7 ms: 1.01x faster                                                |
| python_startup_no_site   | 7.14 ms                                                                | 7.05 ms: 1.01x faster                                                |
| coroutines               | 23.2 ms                                                                | 23.0 ms: 1.01x faster                                                |
| bpe_tokeniser            | 4.53 sec                                                               | 4.47 sec: 1.01x faster                                               |
| sqlite_synth             | 2.80 us                                                                | 2.77 us: 1.01x faster                                                |
| html5lib                 | 67.0 ms                                                                | 66.5 ms: 1.01x faster                                                |
| shortest_path            | 482 ms                                                                 | 479 ms: 1.01x faster                                                 |
| comprehensions           | 17.5 us                                                                | 17.4 us: 1.01x faster                                                |
| regex_dna                | 216 ms                                                                 | 215 ms: 1.00x faster                                                 |
| mako                     | 10.3 ms                                                                | 10.2 ms: 1.00x faster                                                |
| connected_components     | 437 ms                                                                 | 436 ms: 1.00x faster                                                 |
| meteor_contest           | 109 ms                                                                 | 109 ms: 1.00x faster                                                 |
| pidigits                 | 187 ms                                                                 | 187 ms: 1.00x slower                                                 |
| scimark_fft              | 318 ms                                                                 | 319 ms: 1.00x slower                                                 |
| async_tree_io_tg         | 978 ms                                                                 | 986 ms: 1.01x slower                                                 |
| scimark_lu               | 113 ms                                                                 | 114 ms: 1.01x slower                                                 |
| deepcopy_memo            | 29.6 us                                                                | 29.9 us: 1.01x slower                                                |
| scimark_monte_carlo      | 64.8 ms                                                                | 65.4 ms: 1.01x slower                                                |
| deepcopy                 | 267 us                                                                 | 270 us: 1.01x slower                                                 |
| fannkuch                 | 389 ms                                                                 | 394 ms: 1.01x slower                                                 |
| pathlib                  | 16.1 ms                                                                | 16.2 ms: 1.01x slower                                                |
| async_generators         | 456 ms                                                                 | 461 ms: 1.01x slower                                                 |
| logging_format           | 6.17 us                                                                | 6.25 us: 1.01x slower                                                |
| chaos                    | 59.1 ms                                                                | 59.9 ms: 1.01x slower                                                |
| pickle_pure_python       | 321 us                                                                 | 326 us: 1.01x slower                                                 |
| scimark_sor              | 119 ms                                                                 | 121 ms: 1.02x slower                                                 |
| xml_etree_iterparse      | 101 ms                                                                 | 102 ms: 1.02x slower                                                 |
| pprint_pformat           | 1.51 sec                                                               | 1.54 sec: 1.02x slower                                               |
| regex_v8                 | 24.6 ms                                                                | 25.1 ms: 1.02x slower                                                |
| pycparser                | 1.16 sec                                                               | 1.19 sec: 1.02x slower                                               |
| logging_simple           | 5.56 us                                                                | 5.70 us: 1.02x slower                                                |
| deepcopy_reduce          | 2.66 us                                                                | 2.72 us: 1.02x slower                                                |
| nbody                    | 82.3 ms                                                                | 84.5 ms: 1.03x slower                                                |
| spectral_norm            | 115 ms                                                                 | 118 ms: 1.03x slower                                                 |
| nqueens                  | 87.9 ms                                                                | 90.6 ms: 1.03x slower                                                |
| pprint_safe_repr         | 724 ms                                                                 | 749 ms: 1.03x slower                                                 |
| xml_etree_parse          | 148 ms                                                                 | 155 ms: 1.04x slower                                                 |
| mdp                      | 2.62 sec                                                               | 2.73 sec: 1.04x slower                                               |
| pyflate                  | 449 ms                                                                 | 472 ms: 1.05x slower                                                 |
| django_template          | 34.3 ms                                                                | 36.3 ms: 1.06x slower                                                |
| richards_super           | 47.1 ms                                                                | 52.2 ms: 1.11x slower                                                |
| richards                 | 40.7 ms                                                                | 45.5 ms: 1.12x slower                                                |
| Geometric mean           | (ref)                                                                  | 1.01x faster                                                         |

Benchmark hidden because not significant (19): logging_silent, crypto_pyaes, xml_etree_process, sqlglot_parse, json_loads, float, json_dumps, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed, thrift, asyncio_websockets, telco, coverage, async_tree_io, k_core, async_tree_none, async_tree_none_tg
Ignored benchmarks (3) of results/bm-20241107-3.14.0a1+-09d6f5d-JIT/bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d.json: djangocms, many_optionals, subparsers

- Geometric mean (including insignificant results): 1.014x faster
# HPT report

- Reliability score: 83.84% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.96x