# Results vs. 3.12.0

- fork: python
- ref: v3.13.0a3
- machine: darwin-arm64
- commit hash: f009305
- commit date: 2024-01-17
- overall geometric mean: 1.010x slower
- HPT reliability: 90.81%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.50x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 172 ms: 1.02x slower                                       |
| chameleon      | 4.70 ms                                                | 4.93 ms: 1.05x slower                                      |
| docutils       | 1.50 sec                                               | 1.46 sec: 1.03x faster                                     |
| tornado_http   | 69.3 ms                                                | 87.7 ms: 1.27x slower                                      |
| Geometric mean | (ref)                                                  | 1.07x slower                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_none        | 266 ms                                                 | 254 ms: 1.05x faster                                       |
| async_tree_io_tg       | 669 ms                                                 | 672 ms: 1.00x slower                                       |
| async_tree_none_tg     | 258 ms                                                 | 260 ms: 1.01x slower                                       |
| async_tree_io          | 668 ms                                                 | 706 ms: 1.06x slower                                       |
| async_tree_memoization | 312 ms                                                 | 331 ms: 1.06x slower                                       |
| Geometric mean         | (ref)                                                  | 1.01x slower                                               |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 282 ms                                                 | 282 ms: 1.00x slower                                       |
| float          | 55.8 ms                                                | 56.8 ms: 1.02x slower                                      |
| nbody          | 68.8 ms                                                | 75.5 ms: 1.10x slower                                      |
| Geometric mean | (ref)                                                  | 1.04x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 77.9 ms                                                | 73.7 ms: 1.06x faster                                      |
| regex_dna      | 154 ms                                                 | 157 ms: 1.02x slower                                       |
| regex_effbot   | 2.64 ms                                                | 2.77 ms: 1.05x slower                                      |
| regex_v8       | 16.0 ms                                                | 18.0 ms: 1.13x slower                                      |
| Geometric mean | (ref)                                                  | 1.03x slower                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 200 us                                                 | 196 us: 1.02x faster                                       |
| json_loads           | 17.2 us                                                | 17.1 us: 1.01x faster                                      |
| pickle_dict          | 18.1 us                                                | 18.0 us: 1.00x faster                                      |
| xml_etree_generate   | 55.8 ms                                                | 56.2 ms: 1.01x slower                                      |
| xml_etree_process    | 39.7 ms                                                | 39.9 ms: 1.01x slower                                      |
| unpickle             | 9.12 us                                                | 9.19 us: 1.01x slower                                      |
| unpickle_pure_python | 151 us                                                 | 153 us: 1.02x slower                                       |
| unpickle_list        | 3.02 us                                                | 3.09 us: 1.02x slower                                      |
| pickle               | 7.23 us                                                | 7.42 us: 1.03x slower                                      |
| pickle_list          | 2.89 us                                                | 2.97 us: 1.03x slower                                      |
| xml_etree_iterparse  | 74.0 ms                                                | 77.2 ms: 1.04x slower                                      |
| xml_etree_parse      | 106 ms                                                 | 111 ms: 1.04x slower                                       |
| json_dumps           | 6.22 ms                                                | 6.55 ms: 1.05x slower                                      |
| tomli_loads          | 1.39 sec                                               | 1.55 sec: 1.11x slower                                     |
| Geometric mean       | (ref)                                                  | 1.02x slower                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 11.4 ms                                                | 16.6 ms: 1.46x slower                                      |
| python_startup_no_site | 9.37 ms                                                | 14.7 ms: 1.57x slower                                      |
| Geometric mean         | (ref)                                                  | 1.51x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| django_template | 22.3 ms                                                | 21.9 ms: 1.02x faster                                      |
| mako            | 7.71 ms                                                | 7.61 ms: 1.01x faster                                      |
| Geometric mean  | (ref)                                                  | 1.02x faster                                               |

All benchmarks:
===============

| Benchmark                | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 93.0 us                                                | 71.3 us: 1.30x faster                                      |
| raytrace                 | 212 ms                                                 | 172 ms: 1.24x faster                                       |
| comprehensions           | 14.5 us                                                | 12.1 us: 1.21x faster                                      |
| generators               | 31.1 ms                                                | 28.0 ms: 1.11x faster                                      |
| unpack_sequence          | 31.5 ns                                                | 28.4 ns: 1.11x faster                                      |
| deltablue                | 2.71 ms                                                | 2.45 ms: 1.11x faster                                      |
| logging_silent           | 76.4 ns                                                | 70.2 ns: 1.09x faster                                      |
| deepcopy_memo            | 27.7 us                                                | 25.8 us: 1.07x faster                                      |
| sqlglot_parse            | 848 us                                                 | 790 us: 1.07x faster                                       |
| crypto_pyaes             | 51.9 ms                                                | 48.4 ms: 1.07x faster                                      |
| chaos                    | 42.5 ms                                                | 39.8 ms: 1.07x faster                                      |
| sympy_sum                | 77.6 ms                                                | 72.9 ms: 1.07x faster                                      |
| logging_simple           | 3.69 us                                                | 3.48 us: 1.06x faster                                      |
| sympy_str                | 148 ms                                                 | 140 ms: 1.06x faster                                       |
| sqlglot_transpile        | 1.02 ms                                                | 966 us: 1.06x faster                                       |
| regex_compile            | 77.9 ms                                                | 73.7 ms: 1.06x faster                                      |
| logging_format           | 3.98 us                                                | 3.78 us: 1.05x faster                                      |
| sympy_integrate          | 11.4 ms                                                | 10.8 ms: 1.05x faster                                      |
| async_tree_none          | 266 ms                                                 | 254 ms: 1.05x faster                                       |
| json                     | 3.09 ms                                                | 2.96 ms: 1.04x faster                                      |
| nqueens                  | 62.4 ms                                                | 60.1 ms: 1.04x faster                                      |
| deepcopy                 | 235 us                                                 | 227 us: 1.03x faster                                       |
| deepcopy_reduce          | 2.07 us                                                | 2.00 us: 1.03x faster                                      |
| docutils                 | 1.50 sec                                               | 1.46 sec: 1.03x faster                                     |
| coroutines               | 19.2 ms                                                | 18.8 ms: 1.03x faster                                      |
| scimark_lu               | 76.0 ms                                                | 74.2 ms: 1.02x faster                                      |
| bench_thread_pool        | 504 us                                                 | 492 us: 1.02x faster                                       |
| async_generators         | 304 ms                                                 | 297 ms: 1.02x faster                                       |
| sqlglot_normalize        | 186 ms                                                 | 182 ms: 1.02x faster                                       |
| dulwich_log              | 29.8 ms                                                | 29.2 ms: 1.02x faster                                      |
| pickle_pure_python       | 200 us                                                 | 196 us: 1.02x faster                                       |
| django_template          | 22.3 ms                                                | 21.9 ms: 1.02x faster                                      |
| sympy_expand             | 241 ms                                                 | 238 ms: 1.01x faster                                       |
| mako                     | 7.71 ms                                                | 7.61 ms: 1.01x faster                                      |
| mdp                      | 1.58 sec                                               | 1.56 sec: 1.01x faster                                     |
| sqlglot_optimize         | 34.0 ms                                                | 33.7 ms: 1.01x faster                                      |
| json_loads               | 17.2 us                                                | 17.1 us: 1.01x faster                                      |
| scimark_sparse_mat_mult  | 3.14 ms                                                | 3.10 ms: 1.01x faster                                      |
| pickle_dict              | 18.1 us                                                | 18.0 us: 1.00x faster                                      |
| asyncio_websockets       | 409 ms                                                 | 408 ms: 1.00x faster                                       |
| pidigits                 | 282 ms                                                 | 282 ms: 1.00x slower                                       |
| gc_traversal             | 2.40 ms                                                | 2.40 ms: 1.00x slower                                      |
| create_gc_cycles         | 701 us                                                 | 703 us: 1.00x slower                                       |
| meteor_contest           | 71.7 ms                                                | 72.0 ms: 1.00x slower                                      |
| async_tree_io_tg         | 669 ms                                                 | 672 ms: 1.00x slower                                       |
| hexiom                   | 4.54 ms                                                | 4.56 ms: 1.00x slower                                      |
| xml_etree_generate       | 55.8 ms                                                | 56.2 ms: 1.01x slower                                      |
| xml_etree_process        | 39.7 ms                                                | 39.9 ms: 1.01x slower                                      |
| unpickle                 | 9.12 us                                                | 9.19 us: 1.01x slower                                      |
| async_tree_none_tg       | 258 ms                                                 | 260 ms: 1.01x slower                                       |
| mypy2                    | 380 ms                                                 | 385 ms: 1.01x slower                                       |
| 2to3                     | 169 ms                                                 | 172 ms: 1.02x slower                                       |
| regex_dna                | 154 ms                                                 | 157 ms: 1.02x slower                                       |
| unpickle_pure_python     | 151 us                                                 | 153 us: 1.02x slower                                       |
| float                    | 55.8 ms                                                | 56.8 ms: 1.02x slower                                      |
| sqlite_synth             | 1.57 us                                                | 1.60 us: 1.02x slower                                      |
| unpickle_list            | 3.02 us                                                | 3.09 us: 1.02x slower                                      |
| pathlib                  | 24.2 ms                                                | 24.8 ms: 1.02x slower                                      |
| pickle                   | 7.23 us                                                | 7.42 us: 1.03x slower                                      |
| pycparser                | 677 ms                                                 | 695 ms: 1.03x slower                                       |
| richards_super           | 36.0 ms                                                | 37.1 ms: 1.03x slower                                      |
| pickle_list              | 2.89 us                                                | 2.97 us: 1.03x slower                                      |
| pprint_pformat           | 1.01 sec                                               | 1.05 sec: 1.04x slower                                     |
| go                       | 102 ms                                                 | 105 ms: 1.04x slower                                       |
| richards                 | 32.1 ms                                                | 33.3 ms: 1.04x slower                                      |
| pprint_safe_repr         | 497 ms                                                 | 516 ms: 1.04x slower                                       |
| xml_etree_iterparse      | 74.0 ms                                                | 77.2 ms: 1.04x slower                                      |
| scimark_fft              | 195 ms                                                 | 204 ms: 1.04x slower                                       |
| xml_etree_parse          | 106 ms                                                 | 111 ms: 1.04x slower                                       |
| scimark_monte_carlo      | 45.0 ms                                                | 47.3 ms: 1.05x slower                                      |
| chameleon                | 4.70 ms                                                | 4.93 ms: 1.05x slower                                      |
| regex_effbot             | 2.64 ms                                                | 2.77 ms: 1.05x slower                                      |
| json_dumps               | 6.22 ms                                                | 6.55 ms: 1.05x slower                                      |
| async_tree_io            | 668 ms                                                 | 706 ms: 1.06x slower                                       |
| async_tree_memoization   | 312 ms                                                 | 331 ms: 1.06x slower                                       |
| asyncio_tcp_ssl          | 1.24 sec                                               | 1.32 sec: 1.06x slower                                     |
| pyflate                  | 316 ms                                                 | 340 ms: 1.08x slower                                       |
| bench_mp_pool            | 44.9 ms                                                | 48.4 ms: 1.08x slower                                      |
| fannkuch                 | 248 ms                                                 | 272 ms: 1.10x slower                                       |
| nbody                    | 68.8 ms                                                | 75.5 ms: 1.10x slower                                      |
| tomli_loads              | 1.39 sec                                               | 1.55 sec: 1.11x slower                                     |
| regex_v8                 | 16.0 ms                                                | 18.0 ms: 1.13x slower                                      |
| gunicorn                 | 1.15 ms                                                | 1.33 ms: 1.16x slower                                      |
| scimark_sor              | 87.4 ms                                                | 105 ms: 1.20x slower                                       |
| aiohttp                  | 1.08 ms                                                | 1.31 ms: 1.22x slower                                      |
| coverage                 | 38.9 ms                                                | 47.8 ms: 1.23x slower                                      |
| telco                    | 3.68 ms                                                | 4.58 ms: 1.24x slower                                      |
| tornado_http             | 69.3 ms                                                | 87.7 ms: 1.27x slower                                      |
| python_startup           | 11.4 ms                                                | 16.6 ms: 1.46x slower                                      |
| python_startup_no_site   | 9.37 ms                                                | 14.7 ms: 1.57x slower                                      |
| Geometric mean           | (ref)                                                  | 1.01x slower                                               |

Benchmark hidden because not significant (5): asyncio_tcp, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, spectral_norm, async_tree_memoization_tg
Ignored benchmarks (3) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: dask, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (15) of results/bm-20240117-3.13.0a3-f009305-PYTHON_UOPS/bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.010x slower
# HPT report

- Reliability score: 90.81% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.50x