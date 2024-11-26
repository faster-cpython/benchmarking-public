# Results vs. 3.12.0

- fork: python
- ref: v3.13.0a4
- machine: darwin-arm64
- commit hash: 9d34f60
- commit date: 2024-02-15
- overall geometric mean: 1.006x slower
- HPT reliability: 92.04%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.82x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 174 ms: 1.03x slower                                       |
| chameleon      | 4.70 ms                                                | 4.84 ms: 1.03x slower                                      |
| docutils       | 1.50 sec                                               | 1.46 sec: 1.03x faster                                     |
| tornado_http   | 69.3 ms                                                | 84.4 ms: 1.22x slower                                      |
| Geometric mean | (ref)                                                  | 1.06x slower                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_none        | 266 ms                                                 | 253 ms: 1.05x faster                                       |
| async_tree_io_tg       | 669 ms                                                 | 672 ms: 1.00x slower                                       |
| async_tree_none_tg     | 258 ms                                                 | 260 ms: 1.01x slower                                       |
| async_tree_io          | 668 ms                                                 | 707 ms: 1.06x slower                                       |
| async_tree_memoization | 312 ms                                                 | 332 ms: 1.06x slower                                       |
| Geometric mean         | (ref)                                                  | 1.01x slower                                               |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 282 ms                                                 | 282 ms: 1.00x slower                                       |
| float          | 55.8 ms                                                | 56.7 ms: 1.02x slower                                      |
| nbody          | 68.8 ms                                                | 74.0 ms: 1.08x slower                                      |
| Geometric mean | (ref)                                                  | 1.03x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_effbot   | 2.64 ms                                                | 2.49 ms: 1.06x faster                                      |
| regex_compile  | 77.9 ms                                                | 73.4 ms: 1.06x faster                                      |
| regex_dna      | 154 ms                                                 | 146 ms: 1.06x faster                                       |
| regex_v8       | 16.0 ms                                                | 17.1 ms: 1.07x slower                                      |
| Geometric mean | (ref)                                                  | 1.03x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 200 us                                                 | 196 us: 1.02x faster                                       |
| json_loads           | 17.2 us                                                | 16.9 us: 1.02x faster                                      |
| pickle_dict          | 18.1 us                                                | 18.1 us: 1.00x slower                                      |
| xml_etree_generate   | 55.8 ms                                                | 56.2 ms: 1.01x slower                                      |
| xml_etree_parse      | 106 ms                                                 | 108 ms: 1.01x slower                                       |
| pickle               | 7.23 us                                                | 7.32 us: 1.01x slower                                      |
| unpickle_list        | 3.02 us                                                | 3.07 us: 1.02x slower                                      |
| unpickle_pure_python | 151 us                                                 | 154 us: 1.03x slower                                       |
| pickle_list          | 2.89 us                                                | 2.96 us: 1.03x slower                                      |
| json_dumps           | 6.22 ms                                                | 6.46 ms: 1.04x slower                                      |
| xml_etree_iterparse  | 74.0 ms                                                | 77.6 ms: 1.05x slower                                      |
| tomli_loads          | 1.39 sec                                               | 1.54 sec: 1.11x slower                                     |
| Geometric mean       | (ref)                                                  | 1.02x slower                                               |

Benchmark hidden because not significant (2): unpickle, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 11.4 ms                                                | 16.6 ms: 1.46x slower                                      |
| python_startup_no_site | 9.37 ms                                                | 14.8 ms: 1.57x slower                                      |
| Geometric mean         | (ref)                                                  | 1.51x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako            | 7.71 ms                                                | 7.33 ms: 1.05x faster                                      |
| django_template | 22.3 ms                                                | 21.6 ms: 1.03x faster                                      |
| Geometric mean  | (ref)                                                  | 1.04x faster                                               |

All benchmarks:
===============

| Benchmark                | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 93.0 us                                                | 72.2 us: 1.29x faster                                      |
| raytrace                 | 212 ms                                                 | 171 ms: 1.24x faster                                       |
| comprehensions           | 14.5 us                                                | 12.1 us: 1.21x faster                                      |
| unpack_sequence          | 31.5 ns                                                | 28.0 ns: 1.13x faster                                      |
| deltablue                | 2.71 ms                                                | 2.44 ms: 1.11x faster                                      |
| asyncio_tcp              | 449 ms                                                 | 406 ms: 1.11x faster                                       |
| logging_silent           | 76.4 ns                                                | 69.5 ns: 1.10x faster                                      |
| generators               | 31.1 ms                                                | 28.6 ms: 1.09x faster                                      |
| chaos                    | 42.5 ms                                                | 39.4 ms: 1.08x faster                                      |
| crypto_pyaes             | 51.9 ms                                                | 48.2 ms: 1.08x faster                                      |
| deepcopy_memo            | 27.7 us                                                | 25.7 us: 1.08x faster                                      |
| sqlglot_parse            | 848 us                                                 | 790 us: 1.07x faster                                       |
| sympy_sum                | 77.6 ms                                                | 72.4 ms: 1.07x faster                                      |
| logging_simple           | 3.69 us                                                | 3.44 us: 1.07x faster                                      |
| logging_format           | 3.98 us                                                | 3.72 us: 1.07x faster                                      |
| sympy_str                | 148 ms                                                 | 138 ms: 1.07x faster                                       |
| sympy_integrate          | 11.4 ms                                                | 10.7 ms: 1.06x faster                                      |
| regex_effbot             | 2.64 ms                                                | 2.49 ms: 1.06x faster                                      |
| regex_compile            | 77.9 ms                                                | 73.4 ms: 1.06x faster                                      |
| regex_dna                | 154 ms                                                 | 146 ms: 1.06x faster                                       |
| sqlglot_transpile        | 1.02 ms                                                | 968 us: 1.05x faster                                       |
| mako                     | 7.71 ms                                                | 7.33 ms: 1.05x faster                                      |
| deepcopy_reduce          | 2.07 us                                                | 1.97 us: 1.05x faster                                      |
| async_tree_none          | 266 ms                                                 | 253 ms: 1.05x faster                                       |
| deepcopy                 | 235 us                                                 | 224 us: 1.05x faster                                       |
| bench_thread_pool        | 504 us                                                 | 484 us: 1.04x faster                                       |
| json                     | 3.09 ms                                                | 2.97 ms: 1.04x faster                                      |
| nqueens                  | 62.4 ms                                                | 60.1 ms: 1.04x faster                                      |
| django_template          | 22.3 ms                                                | 21.6 ms: 1.03x faster                                      |
| docutils                 | 1.50 sec                                               | 1.46 sec: 1.03x faster                                     |
| spectral_norm            | 76.4 ms                                                | 74.4 ms: 1.03x faster                                      |
| sqlglot_normalize        | 186 ms                                                 | 181 ms: 1.02x faster                                       |
| scimark_lu               | 76.0 ms                                                | 74.2 ms: 1.02x faster                                      |
| async_generators         | 304 ms                                                 | 297 ms: 1.02x faster                                       |
| pickle_pure_python       | 200 us                                                 | 196 us: 1.02x faster                                       |
| json_loads               | 17.2 us                                                | 16.9 us: 1.02x faster                                      |
| mdp                      | 1.58 sec                                               | 1.56 sec: 1.02x faster                                     |
| dulwich_log              | 29.8 ms                                                | 29.4 ms: 1.01x faster                                      |
| sympy_expand             | 241 ms                                                 | 238 ms: 1.01x faster                                       |
| sqlglot_optimize         | 34.0 ms                                                | 33.7 ms: 1.01x faster                                      |
| scimark_sparse_mat_mult  | 3.14 ms                                                | 3.12 ms: 1.01x faster                                      |
| asyncio_websockets       | 409 ms                                                 | 408 ms: 1.00x faster                                       |
| pidigits                 | 282 ms                                                 | 282 ms: 1.00x slower                                       |
| pickle_dict              | 18.1 us                                                | 18.1 us: 1.00x slower                                      |
| gc_traversal             | 2.40 ms                                                | 2.40 ms: 1.00x slower                                      |
| hexiom                   | 4.54 ms                                                | 4.56 ms: 1.00x slower                                      |
| async_tree_io_tg         | 669 ms                                                 | 672 ms: 1.00x slower                                       |
| xml_etree_generate       | 55.8 ms                                                | 56.2 ms: 1.01x slower                                      |
| async_tree_none_tg       | 258 ms                                                 | 260 ms: 1.01x slower                                       |
| create_gc_cycles         | 701 us                                                 | 710 us: 1.01x slower                                       |
| xml_etree_parse          | 106 ms                                                 | 108 ms: 1.01x slower                                       |
| mypy2                    | 380 ms                                                 | 385 ms: 1.01x slower                                       |
| pickle                   | 7.23 us                                                | 7.32 us: 1.01x slower                                      |
| unpickle_list            | 3.02 us                                                | 3.07 us: 1.02x slower                                      |
| float                    | 55.8 ms                                                | 56.7 ms: 1.02x slower                                      |
| meteor_contest           | 71.7 ms                                                | 72.9 ms: 1.02x slower                                      |
| sqlite_synth             | 1.57 us                                                | 1.60 us: 1.02x slower                                      |
| pycparser                | 677 ms                                                 | 693 ms: 1.02x slower                                       |
| unpickle_pure_python     | 151 us                                                 | 154 us: 1.03x slower                                       |
| pickle_list              | 2.89 us                                                | 2.96 us: 1.03x slower                                      |
| 2to3                     | 169 ms                                                 | 174 ms: 1.03x slower                                       |
| go                       | 102 ms                                                 | 105 ms: 1.03x slower                                       |
| chameleon                | 4.70 ms                                                | 4.84 ms: 1.03x slower                                      |
| pprint_pformat           | 1.01 sec                                               | 1.05 sec: 1.03x slower                                     |
| pprint_safe_repr         | 497 ms                                                 | 514 ms: 1.03x slower                                       |
| json_dumps               | 6.22 ms                                                | 6.46 ms: 1.04x slower                                      |
| scimark_fft              | 195 ms                                                 | 203 ms: 1.04x slower                                       |
| scimark_monte_carlo      | 45.0 ms                                                | 47.0 ms: 1.04x slower                                      |
| richards_super           | 36.0 ms                                                | 37.7 ms: 1.05x slower                                      |
| xml_etree_iterparse      | 74.0 ms                                                | 77.6 ms: 1.05x slower                                      |
| pathlib                  | 24.2 ms                                                | 25.4 ms: 1.05x slower                                      |
| richards                 | 32.1 ms                                                | 33.9 ms: 1.06x slower                                      |
| async_tree_io            | 668 ms                                                 | 707 ms: 1.06x slower                                       |
| async_tree_memoization   | 312 ms                                                 | 332 ms: 1.06x slower                                       |
| asyncio_tcp_ssl          | 1.24 sec                                               | 1.32 sec: 1.06x slower                                     |
| regex_v8                 | 16.0 ms                                                | 17.1 ms: 1.07x slower                                      |
| pyflate                  | 316 ms                                                 | 339 ms: 1.07x slower                                       |
| nbody                    | 68.8 ms                                                | 74.0 ms: 1.08x slower                                      |
| fannkuch                 | 248 ms                                                 | 268 ms: 1.08x slower                                       |
| bench_mp_pool            | 44.9 ms                                                | 48.7 ms: 1.08x slower                                      |
| tomli_loads              | 1.39 sec                                               | 1.54 sec: 1.11x slower                                     |
| gunicorn                 | 1.15 ms                                                | 1.36 ms: 1.19x slower                                      |
| aiohttp                  | 1.08 ms                                                | 1.30 ms: 1.20x slower                                      |
| scimark_sor              | 87.4 ms                                                | 105 ms: 1.20x slower                                       |
| telco                    | 3.68 ms                                                | 4.47 ms: 1.21x slower                                      |
| tornado_http             | 69.3 ms                                                | 84.4 ms: 1.22x slower                                      |
| coverage                 | 38.9 ms                                                | 47.7 ms: 1.23x slower                                      |
| python_startup           | 11.4 ms                                                | 16.6 ms: 1.46x slower                                      |
| python_startup_no_site   | 9.37 ms                                                | 14.8 ms: 1.57x slower                                      |
| Geometric mean           | (ref)                                                  | 1.01x slower                                               |

Benchmark hidden because not significant (6): async_tree_cpu_io_mixed, coroutines, unpickle, async_tree_cpu_io_mixed_tg, xml_etree_process, async_tree_memoization_tg
Ignored benchmarks (3) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: dask, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (15) of results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.006x slower
# HPT report

- Reliability score: 92.04% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.82x