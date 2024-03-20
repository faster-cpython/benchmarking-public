# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_plt
- machine: darwin-arm64
- commit hash: 9242976
- commit date: 2024-03-15
- overall geometric mean: 1.02x slower
- HPT reliability: 83.81%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.43x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240315-darwin-arm64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 182 ms: 1.07x slower                                               |
| chameleon      | 4.70 ms                                                | 4.81 ms: 1.02x slower                                              |
| docutils       | 1.50 sec                                               | 1.50 sec: 1.00x faster                                             |
| tornado_http   | 69.3 ms                                                | 85.4 ms: 1.23x slower                                              |
| Geometric mean | (ref)                                                  | 1.08x slower                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240315-darwin-arm64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_none        | 266 ms                                                 | 253 ms: 1.05x faster                                               |
| async_tree_io_tg       | 669 ms                                                 | 676 ms: 1.01x slower                                               |
| async_tree_none_tg     | 258 ms                                                 | 261 ms: 1.01x slower                                               |
| async_tree_memoization | 312 ms                                                 | 331 ms: 1.06x slower                                               |
| async_tree_io          | 668 ms                                                 | 708 ms: 1.06x slower                                               |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                       |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240315-darwin-arm64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 52.6 ms: 1.06x faster                                              |
| pidigits       | 282 ms                                                 | 282 ms: 1.00x slower                                               |
| nbody          | 68.8 ms                                                | 69.2 ms: 1.00x slower                                              |
| Geometric mean | (ref)                                                  | 1.02x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240315-darwin-arm64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_dna      | 154 ms                                                 | 152 ms: 1.01x faster                                               |
| regex_compile  | 77.9 ms                                                | 76.8 ms: 1.01x faster                                              |
| regex_effbot   | 2.64 ms                                                | 2.63 ms: 1.00x faster                                              |
| regex_v8       | 16.0 ms                                                | 17.2 ms: 1.08x slower                                              |
| Geometric mean | (ref)                                                  | 1.01x slower                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240315-darwin-arm64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| tomli_loads          | 1.39 sec                                               | 1.29 sec: 1.08x faster                                             |
| unpickle_pure_python | 151 us                                                 | 147 us: 1.02x faster                                               |
| xml_etree_process    | 39.7 ms                                                | 39.0 ms: 1.02x faster                                              |
| json_loads           | 17.2 us                                                | 17.1 us: 1.01x faster                                              |
| pickle_pure_python   | 200 us                                                 | 198 us: 1.01x faster                                               |
| pickle               | 7.23 us                                                | 7.25 us: 1.00x slower                                              |
| unpickle             | 9.12 us                                                | 9.17 us: 1.01x slower                                              |
| xml_etree_generate   | 55.8 ms                                                | 56.2 ms: 1.01x slower                                              |
| pickle_dict          | 18.1 us                                                | 18.2 us: 1.01x slower                                              |
| unpickle_list        | 3.02 us                                                | 3.08 us: 1.02x slower                                              |
| pickle_list          | 2.89 us                                                | 2.99 us: 1.03x slower                                              |
| json_dumps           | 6.22 ms                                                | 6.51 ms: 1.05x slower                                              |
| Geometric mean       | (ref)                                                  | 1.00x faster                                                       |

Benchmark hidden because not significant (2): xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240315-darwin-arm64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 11.4 ms                                                | 17.2 ms: 1.51x slower                                              |
| python_startup_no_site | 9.37 ms                                                | 15.6 ms: 1.66x slower                                              |
| Geometric mean         | (ref)                                                  | 1.58x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240315-darwin-arm64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 7.71 ms                                                | 6.55 ms: 1.18x faster                                              |
| django_template | 22.3 ms                                                | 21.9 ms: 1.02x faster                                              |
| Geometric mean  | (ref)                                                  | 1.10x faster                                                       |

All benchmarks:
===============

| Benchmark                | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240315-darwin-arm64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| typing_runtime_protocols | 93.0 us                                                | 71.4 us: 1.30x faster                                              |
| comprehensions           | 14.5 us                                                | 12.1 us: 1.20x faster                                              |
| mako                     | 7.71 ms                                                | 6.55 ms: 1.18x faster                                              |
| raytrace                 | 212 ms                                                 | 187 ms: 1.13x faster                                               |
| crypto_pyaes             | 51.9 ms                                                | 46.5 ms: 1.11x faster                                              |
| generators               | 31.1 ms                                                | 28.3 ms: 1.10x faster                                              |
| asyncio_tcp              | 449 ms                                                 | 412 ms: 1.09x faster                                               |
| tomli_loads              | 1.39 sec                                               | 1.29 sec: 1.08x faster                                             |
| deltablue                | 2.71 ms                                                | 2.51 ms: 1.08x faster                                              |
| chaos                    | 42.5 ms                                                | 39.5 ms: 1.08x faster                                              |
| logging_simple           | 3.69 us                                                | 3.45 us: 1.07x faster                                              |
| scimark_monte_carlo      | 45.0 ms                                                | 42.1 ms: 1.07x faster                                              |
| deepcopy_memo            | 27.7 us                                                | 26.0 us: 1.07x faster                                              |
| logging_format           | 3.98 us                                                | 3.74 us: 1.06x faster                                              |
| logging_silent           | 76.4 ns                                                | 72.1 ns: 1.06x faster                                              |
| float                    | 55.8 ms                                                | 52.6 ms: 1.06x faster                                              |
| spectral_norm            | 76.4 ms                                                | 72.2 ms: 1.06x faster                                              |
| sqlglot_parse            | 848 us                                                 | 805 us: 1.05x faster                                               |
| pprint_safe_repr         | 497 ms                                                 | 473 ms: 1.05x faster                                               |
| deepcopy_reduce          | 2.07 us                                                | 1.97 us: 1.05x faster                                              |
| async_tree_none          | 266 ms                                                 | 253 ms: 1.05x faster                                               |
| coroutines               | 19.2 ms                                                | 18.4 ms: 1.05x faster                                              |
| json                     | 3.09 ms                                                | 2.95 ms: 1.05x faster                                              |
| sympy_str                | 148 ms                                                 | 142 ms: 1.04x faster                                               |
| pprint_pformat           | 1.01 sec                                               | 972 ms: 1.04x faster                                               |
| sympy_sum                | 77.6 ms                                                | 75.0 ms: 1.03x faster                                              |
| scimark_sparse_mat_mult  | 3.14 ms                                                | 3.03 ms: 1.03x faster                                              |
| sqlglot_transpile        | 1.02 ms                                                | 988 us: 1.03x faster                                               |
| deepcopy                 | 235 us                                                 | 228 us: 1.03x faster                                               |
| sqlglot_normalize        | 186 ms                                                 | 181 ms: 1.03x faster                                               |
| sympy_integrate          | 11.4 ms                                                | 11.1 ms: 1.03x faster                                              |
| unpickle_pure_python     | 151 us                                                 | 147 us: 1.02x faster                                               |
| django_template          | 22.3 ms                                                | 21.9 ms: 1.02x faster                                              |
| xml_etree_process        | 39.7 ms                                                | 39.0 ms: 1.02x faster                                              |
| regex_dna                | 154 ms                                                 | 152 ms: 1.01x faster                                               |
| regex_compile            | 77.9 ms                                                | 76.8 ms: 1.01x faster                                              |
| json_loads               | 17.2 us                                                | 17.1 us: 1.01x faster                                              |
| pickle_pure_python       | 200 us                                                 | 198 us: 1.01x faster                                               |
| fannkuch                 | 248 ms                                                 | 247 ms: 1.01x faster                                               |
| regex_effbot             | 2.64 ms                                                | 2.63 ms: 1.00x faster                                              |
| docutils                 | 1.50 sec                                               | 1.50 sec: 1.00x faster                                             |
| scimark_fft              | 195 ms                                                 | 195 ms: 1.00x faster                                               |
| pidigits                 | 282 ms                                                 | 282 ms: 1.00x slower                                               |
| pickle                   | 7.23 us                                                | 7.25 us: 1.00x slower                                              |
| nbody                    | 68.8 ms                                                | 69.2 ms: 1.00x slower                                              |
| unpickle                 | 9.12 us                                                | 9.17 us: 1.01x slower                                              |
| xml_etree_generate       | 55.8 ms                                                | 56.2 ms: 1.01x slower                                              |
| gc_traversal             | 2.40 ms                                                | 2.41 ms: 1.01x slower                                              |
| bench_thread_pool        | 504 us                                                 | 508 us: 1.01x slower                                               |
| pyflate                  | 316 ms                                                 | 318 ms: 1.01x slower                                               |
| async_tree_io_tg         | 669 ms                                                 | 676 ms: 1.01x slower                                               |
| sqlite_synth             | 1.57 us                                                | 1.59 us: 1.01x slower                                              |
| nqueens                  | 62.4 ms                                                | 63.1 ms: 1.01x slower                                              |
| pickle_dict              | 18.1 us                                                | 18.2 us: 1.01x slower                                              |
| richards_super           | 36.0 ms                                                | 36.4 ms: 1.01x slower                                              |
| async_tree_none_tg       | 258 ms                                                 | 261 ms: 1.01x slower                                               |
| sqlglot_optimize         | 34.0 ms                                                | 34.5 ms: 1.01x slower                                              |
| mdp                      | 1.58 sec                                               | 1.60 sec: 1.01x slower                                             |
| richards                 | 32.1 ms                                                | 32.6 ms: 1.02x slower                                              |
| sympy_expand             | 241 ms                                                 | 246 ms: 1.02x slower                                               |
| unpickle_list            | 3.02 us                                                | 3.08 us: 1.02x slower                                              |
| hexiom                   | 4.54 ms                                                | 4.64 ms: 1.02x slower                                              |
| async_generators         | 304 ms                                                 | 311 ms: 1.02x slower                                               |
| dulwich_log              | 29.8 ms                                                | 30.5 ms: 1.02x slower                                              |
| chameleon                | 4.70 ms                                                | 4.81 ms: 1.02x slower                                              |
| create_gc_cycles         | 701 us                                                 | 719 us: 1.03x slower                                               |
| dask                     | 222 ms                                                 | 229 ms: 1.03x slower                                               |
| meteor_contest           | 71.7 ms                                                | 74.1 ms: 1.03x slower                                              |
| pathlib                  | 24.2 ms                                                | 25.0 ms: 1.03x slower                                              |
| pickle_list              | 2.89 us                                                | 2.99 us: 1.03x slower                                              |
| pycparser                | 677 ms                                                 | 705 ms: 1.04x slower                                               |
| json_dumps               | 6.22 ms                                                | 6.51 ms: 1.05x slower                                              |
| go                       | 102 ms                                                 | 107 ms: 1.05x slower                                               |
| asyncio_tcp_ssl          | 1.24 sec                                               | 1.31 sec: 1.05x slower                                             |
| async_tree_memoization   | 312 ms                                                 | 331 ms: 1.06x slower                                               |
| async_tree_io            | 668 ms                                                 | 708 ms: 1.06x slower                                               |
| 2to3                     | 169 ms                                                 | 182 ms: 1.07x slower                                               |
| regex_v8                 | 16.0 ms                                                | 17.2 ms: 1.08x slower                                              |
| scimark_lu               | 76.0 ms                                                | 83.9 ms: 1.11x slower                                              |
| bench_mp_pool            | 44.9 ms                                                | 51.3 ms: 1.14x slower                                              |
| telco                    | 3.68 ms                                                | 4.44 ms: 1.21x slower                                              |
| coverage                 | 38.9 ms                                                | 47.5 ms: 1.22x slower                                              |
| tornado_http             | 69.3 ms                                                | 85.4 ms: 1.23x slower                                              |
| scimark_sor              | 87.4 ms                                                | 110 ms: 1.26x slower                                               |
| python_startup           | 11.4 ms                                                | 17.2 ms: 1.51x slower                                              |
| mypy2                    | 380 ms                                                 | 608 ms: 1.60x slower                                               |
| python_startup_no_site   | 9.37 ms                                                | 15.6 ms: 1.66x slower                                              |
| unpack_sequence          | 31.5 ns                                                | 72.7 ns: 2.31x slower                                              |
| Geometric mean           | (ref)                                                  | 1.02x slower                                                       |

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed, asyncio_websockets, async_tree_cpu_io_mixed_tg, xml_etree_parse, xml_etree_iterparse, async_tree_memoization_tg, gunicorn, aiohttp
Ignored benchmarks (2) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (13) of results/bm-20240315-3.13.0a5+-9242976-JIT/bm-20240315-darwin-arm64-brandtbucher-justin_plt-3.13.0a5+-9242976.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, genshi_text, genshi_xml, html5lib, pylint, thrift


# HPT report

- Reliability score: 83.81% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x


# Memory

- memory change: 1.43x