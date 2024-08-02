# Results vs. 3.12.0

- fork: python
- ref: v3.13.0a5
- machine: darwin-arm64
- commit hash: 076d169
- commit date: 2024-03-12
- overall geometric mean: 1.01x slower
- HPT reliability: 98.55%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.49x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240312-darwin-arm64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 173 ms: 1.02x slower                                       |
| chameleon      | 4.70 ms                                                | 5.13 ms: 1.09x slower                                      |
| docutils       | 1.50 sec                                               | 1.47 sec: 1.02x faster                                     |
| Geometric mean | (ref)                                                  | 1.02x slower                                               |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240312-darwin-arm64-python-v3.13.0a5-3.13.0a5-076d169 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_none        | 266 ms                                                 | 257 ms: 1.03x faster                                       |
| async_tree_io_tg       | 669 ms                                                 | 672 ms: 1.00x slower                                       |
| async_tree_none_tg     | 258 ms                                                 | 259 ms: 1.01x slower                                       |
| async_tree_io          | 668 ms                                                 | 710 ms: 1.06x slower                                       |
| async_tree_memoization | 312 ms                                                 | 335 ms: 1.07x slower                                       |
| Geometric mean         | (ref)                                                  | 1.01x slower                                               |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240312-darwin-arm64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 282 ms                                                 | 282 ms: 1.00x slower                                       |
| float          | 55.8 ms                                                | 57.0 ms: 1.02x slower                                      |
| nbody          | 68.8 ms                                                | 73.7 ms: 1.07x slower                                      |
| Geometric mean | (ref)                                                  | 1.03x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240312-darwin-arm64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 77.9 ms                                                | 75.1 ms: 1.04x faster                                      |
| regex_effbot   | 2.64 ms                                                | 2.56 ms: 1.03x faster                                      |
| regex_dna      | 154 ms                                                 | 152 ms: 1.02x faster                                       |
| regex_v8       | 16.0 ms                                                | 17.1 ms: 1.07x slower                                      |
| Geometric mean | (ref)                                                  | 1.00x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240312-darwin-arm64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| json_loads           | 17.2 us                                                | 17.1 us: 1.01x faster                                      |
| pickle_pure_python   | 200 us                                                 | 201 us: 1.01x slower                                       |
| pickle_dict          | 18.1 us                                                | 18.2 us: 1.01x slower                                      |
| unpickle_list        | 3.02 us                                                | 3.05 us: 1.01x slower                                      |
| pickle               | 7.23 us                                                | 7.31 us: 1.01x slower                                      |
| xml_etree_process    | 39.7 ms                                                | 40.4 ms: 1.02x slower                                      |
| unpickle             | 9.12 us                                                | 9.30 us: 1.02x slower                                      |
| pickle_list          | 2.89 us                                                | 2.96 us: 1.03x slower                                      |
| xml_etree_iterparse  | 74.0 ms                                                | 75.9 ms: 1.03x slower                                      |
| xml_etree_generate   | 55.8 ms                                                | 58.1 ms: 1.04x slower                                      |
| unpickle_pure_python | 151 us                                                 | 157 us: 1.04x slower                                       |
| json_dumps           | 6.22 ms                                                | 6.52 ms: 1.05x slower                                      |
| tomli_loads          | 1.39 sec                                               | 1.55 sec: 1.11x slower                                     |
| Geometric mean       | (ref)                                                  | 1.03x slower                                               |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240312-darwin-arm64-python-v3.13.0a5-3.13.0a5-076d169 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 11.4 ms                                                | 12.9 ms: 1.13x slower                                      |
| python_startup_no_site | 9.37 ms                                                | 11.3 ms: 1.20x slower                                      |
| Geometric mean         | (ref)                                                  | 1.17x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240312-darwin-arm64-python-v3.13.0a5-3.13.0a5-076d169 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako            | 7.71 ms                                                | 7.57 ms: 1.02x faster                                      |
| django_template | 22.3 ms                                                | 22.2 ms: 1.01x faster                                      |
| Geometric mean  | (ref)                                                  | 1.01x faster                                               |

All benchmarks:
===============

| Benchmark                | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240312-darwin-arm64-python-v3.13.0a5-3.13.0a5-076d169 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 93.0 us                                                | 72.9 us: 1.28x faster                                      |
| raytrace                 | 212 ms                                                 | 171 ms: 1.24x faster                                       |
| comprehensions           | 14.5 us                                                | 12.1 us: 1.21x faster                                      |
| deltablue                | 2.71 ms                                                | 2.45 ms: 1.10x faster                                      |
| logging_silent           | 76.4 ns                                                | 70.0 ns: 1.09x faster                                      |
| generators               | 31.1 ms                                                | 28.6 ms: 1.09x faster                                      |
| sqlglot_parse            | 848 us                                                 | 795 us: 1.07x faster                                       |
| deepcopy_memo            | 27.7 us                                                | 25.9 us: 1.07x faster                                      |
| crypto_pyaes             | 51.9 ms                                                | 48.7 ms: 1.07x faster                                      |
| chaos                    | 42.5 ms                                                | 39.9 ms: 1.07x faster                                      |
| gunicorn                 | 1.15 ms                                                | 1.08 ms: 1.06x faster                                      |
| logging_simple           | 3.69 us                                                | 3.50 us: 1.05x faster                                      |
| sqlglot_transpile        | 1.02 ms                                                | 972 us: 1.05x faster                                       |
| logging_format           | 3.98 us                                                | 3.80 us: 1.05x faster                                      |
| json                     | 3.09 ms                                                | 2.95 ms: 1.05x faster                                      |
| sympy_integrate          | 11.4 ms                                                | 10.9 ms: 1.04x faster                                      |
| regex_compile            | 77.9 ms                                                | 75.1 ms: 1.04x faster                                      |
| sympy_sum                | 77.6 ms                                                | 75.0 ms: 1.04x faster                                      |
| async_tree_none          | 266 ms                                                 | 257 ms: 1.03x faster                                       |
| sympy_str                | 148 ms                                                 | 143 ms: 1.03x faster                                       |
| regex_effbot             | 2.64 ms                                                | 2.56 ms: 1.03x faster                                      |
| aiohttp                  | 1.08 ms                                                | 1.06 ms: 1.02x faster                                      |
| scimark_lu               | 76.0 ms                                                | 74.3 ms: 1.02x faster                                      |
| docutils                 | 1.50 sec                                               | 1.47 sec: 1.02x faster                                     |
| deepcopy                 | 235 us                                                 | 230 us: 1.02x faster                                       |
| mako                     | 7.71 ms                                                | 7.57 ms: 1.02x faster                                      |
| bench_thread_pool        | 504 us                                                 | 495 us: 1.02x faster                                       |
| regex_dna                | 154 ms                                                 | 152 ms: 1.02x faster                                       |
| dulwich_log              | 29.8 ms                                                | 29.6 ms: 1.01x faster                                      |
| django_template          | 22.3 ms                                                | 22.2 ms: 1.01x faster                                      |
| json_loads               | 17.2 us                                                | 17.1 us: 1.01x faster                                      |
| spectral_norm            | 76.4 ms                                                | 75.8 ms: 1.01x faster                                      |
| sqlglot_normalize        | 186 ms                                                 | 185 ms: 1.01x faster                                       |
| deepcopy_reduce          | 2.07 us                                                | 2.06 us: 1.01x faster                                      |
| async_generators         | 304 ms                                                 | 302 ms: 1.01x faster                                       |
| asyncio_websockets       | 409 ms                                                 | 408 ms: 1.00x faster                                       |
| pidigits                 | 282 ms                                                 | 282 ms: 1.00x slower                                       |
| sqlite_synth             | 1.57 us                                                | 1.57 us: 1.00x slower                                      |
| async_tree_io_tg         | 669 ms                                                 | 672 ms: 1.00x slower                                       |
| sqlglot_optimize         | 34.0 ms                                                | 34.2 ms: 1.00x slower                                      |
| pickle_pure_python       | 200 us                                                 | 201 us: 1.01x slower                                       |
| async_tree_none_tg       | 258 ms                                                 | 259 ms: 1.01x slower                                       |
| gc_traversal             | 2.40 ms                                                | 2.42 ms: 1.01x slower                                      |
| pickle_dict              | 18.1 us                                                | 18.2 us: 1.01x slower                                      |
| unpickle_list            | 3.02 us                                                | 3.05 us: 1.01x slower                                      |
| sympy_expand             | 241 ms                                                 | 243 ms: 1.01x slower                                       |
| pickle                   | 7.23 us                                                | 7.31 us: 1.01x slower                                      |
| create_gc_cycles         | 701 us                                                 | 710 us: 1.01x slower                                       |
| bench_mp_pool            | 44.9 ms                                                | 45.4 ms: 1.01x slower                                      |
| dask                     | 222 ms                                                 | 225 ms: 1.01x slower                                       |
| xml_etree_process        | 39.7 ms                                                | 40.4 ms: 1.02x slower                                      |
| 2to3                     | 169 ms                                                 | 173 ms: 1.02x slower                                       |
| unpickle                 | 9.12 us                                                | 9.30 us: 1.02x slower                                      |
| float                    | 55.8 ms                                                | 57.0 ms: 1.02x slower                                      |
| pathlib                  | 24.2 ms                                                | 24.8 ms: 1.02x slower                                      |
| pickle_list              | 2.89 us                                                | 2.96 us: 1.03x slower                                      |
| xml_etree_iterparse      | 74.0 ms                                                | 75.9 ms: 1.03x slower                                      |
| meteor_contest           | 71.7 ms                                                | 73.6 ms: 1.03x slower                                      |
| pycparser                | 677 ms                                                 | 700 ms: 1.03x slower                                       |
| go                       | 102 ms                                                 | 105 ms: 1.04x slower                                       |
| xml_etree_generate       | 55.8 ms                                                | 58.1 ms: 1.04x slower                                      |
| unpickle_pure_python     | 151 us                                                 | 157 us: 1.04x slower                                       |
| mdp                      | 1.58 sec                                               | 1.64 sec: 1.04x slower                                     |
| nqueens                  | 62.4 ms                                                | 65.2 ms: 1.04x slower                                      |
| pprint_pformat           | 1.01 sec                                               | 1.06 sec: 1.05x slower                                     |
| json_dumps               | 6.22 ms                                                | 6.52 ms: 1.05x slower                                      |
| pprint_safe_repr         | 497 ms                                                 | 522 ms: 1.05x slower                                       |
| richards_super           | 36.0 ms                                                | 38.0 ms: 1.05x slower                                      |
| scimark_fft              | 195 ms                                                 | 207 ms: 1.06x slower                                       |
| hexiom                   | 4.54 ms                                                | 4.83 ms: 1.06x slower                                      |
| async_tree_io            | 668 ms                                                 | 710 ms: 1.06x slower                                       |
| asyncio_tcp_ssl          | 1.24 sec                                               | 1.32 sec: 1.06x slower                                     |
| regex_v8                 | 16.0 ms                                                | 17.1 ms: 1.07x slower                                      |
| nbody                    | 68.8 ms                                                | 73.7 ms: 1.07x slower                                      |
| async_tree_memoization   | 312 ms                                                 | 335 ms: 1.07x slower                                       |
| scimark_monte_carlo      | 45.0 ms                                                | 48.3 ms: 1.07x slower                                      |
| richards                 | 32.1 ms                                                | 34.5 ms: 1.07x slower                                      |
| pyflate                  | 316 ms                                                 | 342 ms: 1.08x slower                                       |
| chameleon                | 4.70 ms                                                | 5.13 ms: 1.09x slower                                      |
| fannkuch                 | 248 ms                                                 | 274 ms: 1.10x slower                                       |
| tomli_loads              | 1.39 sec                                               | 1.55 sec: 1.11x slower                                     |
| python_startup           | 11.4 ms                                                | 12.9 ms: 1.13x slower                                      |
| mypy2                    | 380 ms                                                 | 457 ms: 1.20x slower                                       |
| python_startup_no_site   | 9.37 ms                                                | 11.3 ms: 1.20x slower                                      |
| scimark_sor              | 87.4 ms                                                | 105 ms: 1.20x slower                                       |
| coverage                 | 38.9 ms                                                | 48.4 ms: 1.25x slower                                      |
| telco                    | 3.68 ms                                                | 4.63 ms: 1.26x slower                                      |
| Geometric mean           | (ref)                                                  | 1.01x slower                                               |

Benchmark hidden because not significant (8): asyncio_tcp, tornado_http, async_tree_cpu_io_mixed_tg, coroutines, scimark_sparse_mat_mult, async_tree_cpu_io_mixed, xml_etree_parse, async_tree_memoization_tg
Ignored benchmarks (3) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (14) of results/bm-20240312-3.13.0a5-076d169/bm-20240312-darwin-arm64-python-v3.13.0a5-3.13.0a5-076d169.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 98.55% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.49x