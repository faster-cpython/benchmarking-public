# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_mprotect_cost
- machine: darwin-arm64
- commit hash: c8d6017
- commit date: 2024-03-18
- overall geometric mean: 1.05x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.82x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240318-darwin-arm64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 188 ms: 1.11x slower                                                         |
| chameleon      | 4.70 ms                                                | 4.82 ms: 1.03x slower                                                        |
| docutils       | 1.50 sec                                               | 1.54 sec: 1.02x slower                                                       |
| tornado_http   | 69.3 ms                                                | 84.9 ms: 1.23x slower                                                        |
| Geometric mean | (ref)                                                  | 1.09x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240318-darwin-arm64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_none        | 266 ms                                                 | 254 ms: 1.05x faster                                                         |
| async_tree_io_tg       | 669 ms                                                 | 676 ms: 1.01x slower                                                         |
| async_tree_none_tg     | 258 ms                                                 | 260 ms: 1.01x slower                                                         |
| async_tree_io          | 668 ms                                                 | 706 ms: 1.06x slower                                                         |
| async_tree_memoization | 312 ms                                                 | 331 ms: 1.06x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240318-darwin-arm64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 53.1 ms: 1.05x faster                                                        |
| pidigits       | 282 ms                                                 | 282 ms: 1.00x slower                                                         |
| nbody          | 68.8 ms                                                | 70.8 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240318-darwin-arm64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_dna      | 154 ms                                                 | 152 ms: 1.01x faster                                                         |
| regex_effbot   | 2.64 ms                                                | 2.63 ms: 1.00x faster                                                        |
| regex_v8       | 16.0 ms                                                | 17.2 ms: 1.08x slower                                                        |
| regex_compile  | 77.9 ms                                                | 85.4 ms: 1.10x slower                                                        |
| Geometric mean | (ref)                                                  | 1.04x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240318-darwin-arm64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 1.39 sec                                               | 1.36 sec: 1.03x faster                                                       |
| pickle_pure_python   | 200 us                                                 | 196 us: 1.02x faster                                                         |
| xml_etree_process    | 39.7 ms                                                | 39.0 ms: 1.02x faster                                                        |
| json_loads           | 17.2 us                                                | 17.1 us: 1.01x faster                                                        |
| unpickle             | 9.12 us                                                | 9.15 us: 1.00x slower                                                        |
| unpickle_pure_python | 151 us                                                 | 151 us: 1.00x slower                                                         |
| pickle_dict          | 18.1 us                                                | 18.2 us: 1.01x slower                                                        |
| pickle               | 7.23 us                                                | 7.29 us: 1.01x slower                                                        |
| xml_etree_iterparse  | 74.0 ms                                                | 74.7 ms: 1.01x slower                                                        |
| unpickle_list        | 3.02 us                                                | 3.06 us: 1.01x slower                                                        |
| xml_etree_generate   | 55.8 ms                                                | 56.8 ms: 1.02x slower                                                        |
| pickle_list          | 2.89 us                                                | 2.98 us: 1.03x slower                                                        |
| json_dumps           | 6.22 ms                                                | 6.53 ms: 1.05x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240318-darwin-arm64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 11.4 ms                                                | 20.6 ms: 1.81x slower                                                        |
| python_startup_no_site | 9.37 ms                                                | 18.9 ms: 2.02x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.91x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240318-darwin-arm64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 7.71 ms                                                | 6.73 ms: 1.15x faster                                                        |
| django_template | 22.3 ms                                                | 22.1 ms: 1.01x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240318-darwin-arm64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 93.0 us                                                | 71.7 us: 1.30x faster                                                        |
| mako                     | 7.71 ms                                                | 6.73 ms: 1.15x faster                                                        |
| comprehensions           | 14.5 us                                                | 12.7 us: 1.15x faster                                                        |
| raytrace                 | 212 ms                                                 | 192 ms: 1.10x faster                                                         |
| generators               | 31.1 ms                                                | 28.4 ms: 1.09x faster                                                        |
| crypto_pyaes             | 51.9 ms                                                | 47.9 ms: 1.08x faster                                                        |
| deltablue                | 2.71 ms                                                | 2.54 ms: 1.07x faster                                                        |
| chaos                    | 42.5 ms                                                | 40.1 ms: 1.06x faster                                                        |
| logging_format           | 3.98 us                                                | 3.76 us: 1.06x faster                                                        |
| logging_silent           | 76.4 ns                                                | 72.3 ns: 1.06x faster                                                        |
| deepcopy_memo            | 27.7 us                                                | 26.2 us: 1.06x faster                                                        |
| logging_simple           | 3.69 us                                                | 3.49 us: 1.06x faster                                                        |
| float                    | 55.8 ms                                                | 53.1 ms: 1.05x faster                                                        |
| deepcopy_reduce          | 2.07 us                                                | 1.98 us: 1.05x faster                                                        |
| async_tree_none          | 266 ms                                                 | 254 ms: 1.05x faster                                                         |
| json                     | 3.09 ms                                                | 2.96 ms: 1.04x faster                                                        |
| coroutines               | 19.2 ms                                                | 18.4 ms: 1.04x faster                                                        |
| tomli_loads              | 1.39 sec                                               | 1.36 sec: 1.03x faster                                                       |
| deepcopy                 | 235 us                                                 | 229 us: 1.02x faster                                                         |
| sympy_str                | 148 ms                                                 | 145 ms: 1.02x faster                                                         |
| pickle_pure_python       | 200 us                                                 | 196 us: 1.02x faster                                                         |
| xml_etree_process        | 39.7 ms                                                | 39.0 ms: 1.02x faster                                                        |
| regex_dna                | 154 ms                                                 | 152 ms: 1.01x faster                                                         |
| sqlglot_normalize        | 186 ms                                                 | 183 ms: 1.01x faster                                                         |
| django_template          | 22.3 ms                                                | 22.1 ms: 1.01x faster                                                        |
| scimark_monte_carlo      | 45.0 ms                                                | 44.5 ms: 1.01x faster                                                        |
| sqlglot_parse            | 848 us                                                 | 840 us: 1.01x faster                                                         |
| json_loads               | 17.2 us                                                | 17.1 us: 1.01x faster                                                        |
| spectral_norm            | 76.4 ms                                                | 76.0 ms: 1.01x faster                                                        |
| regex_effbot             | 2.64 ms                                                | 2.63 ms: 1.00x faster                                                        |
| asyncio_websockets       | 409 ms                                                 | 409 ms: 1.00x faster                                                         |
| pidigits                 | 282 ms                                                 | 282 ms: 1.00x slower                                                         |
| unpickle                 | 9.12 us                                                | 9.15 us: 1.00x slower                                                        |
| unpickle_pure_python     | 151 us                                                 | 151 us: 1.00x slower                                                         |
| sqlglot_transpile        | 1.02 ms                                                | 1.03 ms: 1.00x slower                                                        |
| gc_traversal             | 2.40 ms                                                | 2.41 ms: 1.00x slower                                                        |
| pickle_dict              | 18.1 us                                                | 18.2 us: 1.01x slower                                                        |
| pickle                   | 7.23 us                                                | 7.29 us: 1.01x slower                                                        |
| xml_etree_iterparse      | 74.0 ms                                                | 74.7 ms: 1.01x slower                                                        |
| sympy_integrate          | 11.4 ms                                                | 11.5 ms: 1.01x slower                                                        |
| async_tree_io_tg         | 669 ms                                                 | 676 ms: 1.01x slower                                                         |
| async_tree_none_tg       | 258 ms                                                 | 260 ms: 1.01x slower                                                         |
| sqlite_synth             | 1.57 us                                                | 1.59 us: 1.01x slower                                                        |
| unpickle_list            | 3.02 us                                                | 3.06 us: 1.01x slower                                                        |
| bench_thread_pool        | 504 us                                                 | 512 us: 1.02x slower                                                         |
| create_gc_cycles         | 701 us                                                 | 713 us: 1.02x slower                                                         |
| xml_etree_generate       | 55.8 ms                                                | 56.8 ms: 1.02x slower                                                        |
| scimark_fft              | 195 ms                                                 | 199 ms: 1.02x slower                                                         |
| nqueens                  | 62.4 ms                                                | 63.7 ms: 1.02x slower                                                        |
| docutils                 | 1.50 sec                                               | 1.54 sec: 1.02x slower                                                       |
| chameleon                | 4.70 ms                                                | 4.82 ms: 1.03x slower                                                        |
| sympy_expand             | 241 ms                                                 | 247 ms: 1.03x slower                                                         |
| dask                     | 222 ms                                                 | 228 ms: 1.03x slower                                                         |
| dulwich_log              | 29.8 ms                                                | 30.7 ms: 1.03x slower                                                        |
| nbody                    | 68.8 ms                                                | 70.8 ms: 1.03x slower                                                        |
| async_generators         | 304 ms                                                 | 314 ms: 1.03x slower                                                         |
| pickle_list              | 2.89 us                                                | 2.98 us: 1.03x slower                                                        |
| pprint_safe_repr         | 497 ms                                                 | 515 ms: 1.04x slower                                                         |
| mdp                      | 1.58 sec                                               | 1.64 sec: 1.04x slower                                                       |
| pathlib                  | 24.2 ms                                                | 25.2 ms: 1.04x slower                                                        |
| sqlglot_optimize         | 34.0 ms                                                | 35.5 ms: 1.04x slower                                                        |
| pprint_pformat           | 1.01 sec                                               | 1.06 sec: 1.05x slower                                                       |
| json_dumps               | 6.22 ms                                                | 6.53 ms: 1.05x slower                                                        |
| meteor_contest           | 71.7 ms                                                | 75.3 ms: 1.05x slower                                                        |
| asyncio_tcp_ssl          | 1.24 sec                                               | 1.31 sec: 1.05x slower                                                       |
| async_tree_io            | 668 ms                                                 | 706 ms: 1.06x slower                                                         |
| async_tree_memoization   | 312 ms                                                 | 331 ms: 1.06x slower                                                         |
| pycparser                | 677 ms                                                 | 727 ms: 1.07x slower                                                         |
| regex_v8                 | 16.0 ms                                                | 17.2 ms: 1.08x slower                                                        |
| regex_compile            | 77.9 ms                                                | 85.4 ms: 1.10x slower                                                        |
| pyflate                  | 316 ms                                                 | 348 ms: 1.10x slower                                                         |
| 2to3                     | 169 ms                                                 | 188 ms: 1.11x slower                                                         |
| hexiom                   | 4.54 ms                                                | 5.12 ms: 1.13x slower                                                        |
| scimark_lu               | 76.0 ms                                                | 85.6 ms: 1.13x slower                                                        |
| go                       | 102 ms                                                 | 115 ms: 1.13x slower                                                         |
| richards_super           | 36.0 ms                                                | 42.1 ms: 1.17x slower                                                        |
| richards                 | 32.1 ms                                                | 37.7 ms: 1.17x slower                                                        |
| coverage                 | 38.9 ms                                                | 47.6 ms: 1.22x slower                                                        |
| tornado_http             | 69.3 ms                                                | 84.9 ms: 1.23x slower                                                        |
| telco                    | 3.68 ms                                                | 4.58 ms: 1.24x slower                                                        |
| bench_mp_pool            | 44.9 ms                                                | 56.1 ms: 1.25x slower                                                        |
| fannkuch                 | 248 ms                                                 | 314 ms: 1.26x slower                                                         |
| scimark_sor              | 87.4 ms                                                | 113 ms: 1.29x slower                                                         |
| mypy2                    | 380 ms                                                 | 617 ms: 1.62x slower                                                         |
| python_startup           | 11.4 ms                                                | 20.6 ms: 1.81x slower                                                        |
| python_startup_no_site   | 9.37 ms                                                | 18.9 ms: 2.02x slower                                                        |
| unpack_sequence          | 31.5 ns                                                | 113 ns: 3.59x slower                                                         |
| Geometric mean           | (ref)                                                  | 1.05x slower                                                                 |

Benchmark hidden because not significant (9): async_tree_cpu_io_mixed, sympy_sum, async_tree_cpu_io_mixed_tg, xml_etree_parse, scimark_sparse_mat_mult, async_tree_memoization_tg, aiohttp, asyncio_tcp, gunicorn
Ignored benchmarks (2) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (13) of results/bm-20240318-3.13.0a5+-c8d6017-JIT/bm-20240318-darwin-arm64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, genshi_text, genshi_xml, html5lib, pylint, thrift


# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x


# Memory

- memory change: 1.82x