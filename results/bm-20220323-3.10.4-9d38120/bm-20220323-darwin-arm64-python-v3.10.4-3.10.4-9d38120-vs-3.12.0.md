
# Results vs. 3.12.0

- fork: python
- ref: v3.10.4
- machine: darwin-arm64
- commit hash: 9d38120
- commit date: 2022-03-23
- overall geometric mean: 1.19x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x slower
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 192 ms: 1.13x slower                                   |
| chameleon      | 4.70 ms                                                | 6.26 ms: 1.33x slower                                  |
| docutils       | 1.50 sec                                               | 1.73 sec: 1.15x slower                                 |
| tornado_http   | 69.3 ms                                                | 86.7 ms: 1.25x slower                                  |
| Geometric mean | (ref)                                                  | 1.21x slower                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| async_tree_cpu_io_mixed | 526 ms                                                 | 649 ms: 1.24x slower                                   |
| async_tree_none         | 266 ms                                                 | 388 ms: 1.46x slower                                   |
| async_tree_io           | 668 ms                                                 | 980 ms: 1.47x slower                                   |
| async_tree_memoization  | 312 ms                                                 | 474 ms: 1.52x slower                                   |
| Geometric mean          | (ref)                                                  | 1.42x slower                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pidigits       | 282 ms                                                 | 282 ms: 1.00x slower                                   |
| float          | 55.8 ms                                                | 69.0 ms: 1.24x slower                                  |
| nbody          | 68.8 ms                                                | 93.0 ms: 1.35x slower                                  |
| Geometric mean | (ref)                                                  | 1.19x slower                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot   | 2.64 ms                                                | 2.46 ms: 1.07x faster                                  |
| regex_v8       | 16.0 ms                                                | 17.1 ms: 1.07x slower                                  |
| regex_dna      | 154 ms                                                 | 174 ms: 1.13x slower                                   |
| regex_compile  | 77.9 ms                                                | 95.3 ms: 1.22x slower                                  |
| Geometric mean | (ref)                                                  | 1.08x slower                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| unpickle_list        | 3.02 us                                                | 2.69 us: 1.12x faster                                  |
| pickle_dict          | 18.1 us                                                | 17.0 us: 1.06x faster                                  |
| pickle_list          | 2.89 us                                                | 2.74 us: 1.05x faster                                  |
| json_loads           | 17.2 us                                                | 16.4 us: 1.05x faster                                  |
| xml_etree_generate   | 55.8 ms                                                | 53.5 ms: 1.04x faster                                  |
| unpickle             | 9.12 us                                                | 8.80 us: 1.04x faster                                  |
| pickle               | 7.23 us                                                | 6.97 us: 1.04x faster                                  |
| xml_etree_iterparse  | 74.0 ms                                                | 72.1 ms: 1.03x faster                                  |
| xml_etree_parse      | 106 ms                                                 | 108 ms: 1.01x slower                                   |
| xml_etree_process    | 39.7 ms                                                | 46.5 ms: 1.17x slower                                  |
| tomli_loads          | 1.39 sec                                               | 1.71 sec: 1.22x slower                                 |
| unpickle_pure_python | 151 us                                                 | 194 us: 1.29x slower                                   |
| json_dumps           | 6.22 ms                                                | 8.11 ms: 1.30x slower                                  |
| pickle_pure_python   | 200 us                                                 | 281 us: 1.40x slower                                   |
| Geometric mean       | (ref)                                                  | 1.06x slower                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 7.91 ms: 1.19x faster                                  |
| python_startup         | 11.4 ms                                                | 10.9 ms: 1.05x faster                                  |
| Geometric mean         | (ref)                                                  | 1.12x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| django_template | 22.3 ms                                                | 26.4 ms: 1.18x slower                                  |
| mako            | 7.71 ms                                                | 9.87 ms: 1.28x slower                                  |
| Geometric mean  | (ref)                                                  | 1.23x slower                                           |

All benchmarks:
===============

| Benchmark                | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| async_generators         | 304 ms                                                 | 231 ms: 1.31x faster                                   |
| bench_mp_pool            | 44.9 ms                                                | 37.4 ms: 1.20x faster                                  |
| python_startup_no_site   | 9.37 ms                                                | 7.91 ms: 1.19x faster                                  |
| unpickle_list            | 3.02 us                                                | 2.69 us: 1.12x faster                                  |
| sqlite_synth             | 1.57 us                                                | 1.46 us: 1.08x faster                                  |
| regex_effbot             | 2.64 ms                                                | 2.46 ms: 1.07x faster                                  |
| pickle_dict              | 18.1 us                                                | 17.0 us: 1.06x faster                                  |
| telco                    | 3.68 ms                                                | 3.49 ms: 1.05x faster                                  |
| pickle_list              | 2.89 us                                                | 2.74 us: 1.05x faster                                  |
| python_startup           | 11.4 ms                                                | 10.9 ms: 1.05x faster                                  |
| json_loads               | 17.2 us                                                | 16.4 us: 1.05x faster                                  |
| xml_etree_generate       | 55.8 ms                                                | 53.5 ms: 1.04x faster                                  |
| unpickle                 | 9.12 us                                                | 8.80 us: 1.04x faster                                  |
| pickle                   | 7.23 us                                                | 6.97 us: 1.04x faster                                  |
| xml_etree_iterparse      | 74.0 ms                                                | 72.1 ms: 1.03x faster                                  |
| gc_traversal             | 2.40 ms                                                | 2.36 ms: 1.02x faster                                  |
| pidigits                 | 282 ms                                                 | 282 ms: 1.00x slower                                   |
| xml_etree_parse          | 106 ms                                                 | 108 ms: 1.01x slower                                   |
| nqueens                  | 62.4 ms                                                | 63.8 ms: 1.02x slower                                  |
| sqlglot_normalize        | 186 ms                                                 | 190 ms: 1.02x slower                                   |
| mdp                      | 1.58 sec                                               | 1.63 sec: 1.03x slower                                 |
| generators               | 31.1 ms                                                | 32.3 ms: 1.04x slower                                  |
| bench_thread_pool        | 504 us                                                 | 527 us: 1.05x slower                                   |
| coverage                 | 38.9 ms                                                | 41.5 ms: 1.07x slower                                  |
| regex_v8                 | 16.0 ms                                                | 17.1 ms: 1.07x slower                                  |
| coroutines               | 19.2 ms                                                | 20.7 ms: 1.08x slower                                  |
| sqlglot_optimize         | 34.0 ms                                                | 36.8 ms: 1.08x slower                                  |
| meteor_contest           | 71.7 ms                                                | 77.7 ms: 1.08x slower                                  |
| scimark_sparse_mat_mult  | 3.14 ms                                                | 3.42 ms: 1.09x slower                                  |
| sympy_expand             | 241 ms                                                 | 269 ms: 1.12x slower                                   |
| sympy_str                | 148 ms                                                 | 165 ms: 1.12x slower                                   |
| deepcopy_reduce          | 2.07 us                                                | 2.33 us: 1.13x slower                                  |
| regex_dna                | 154 ms                                                 | 174 ms: 1.13x slower                                   |
| 2to3                     | 169 ms                                                 | 192 ms: 1.13x slower                                   |
| aiohttp                  | 1.08 ms                                                | 1.22 ms: 1.13x slower                                  |
| gunicorn                 | 1.15 ms                                                | 1.30 ms: 1.14x slower                                  |
| dask                     | 222 ms                                                 | 253 ms: 1.14x slower                                   |
| scimark_fft              | 195 ms                                                 | 224 ms: 1.15x slower                                   |
| docutils                 | 1.50 sec                                               | 1.73 sec: 1.15x slower                                 |
| sympy_integrate          | 11.4 ms                                                | 13.1 ms: 1.16x slower                                  |
| deepcopy                 | 235 us                                                 | 272 us: 1.16x slower                                   |
| comprehensions           | 14.5 us                                                | 16.9 us: 1.16x slower                                  |
| xml_etree_process        | 39.7 ms                                                | 46.5 ms: 1.17x slower                                  |
| sqlalchemy_declarative   | 62.3 ms                                                | 73.3 ms: 1.18x slower                                  |
| django_template          | 22.3 ms                                                | 26.4 ms: 1.18x slower                                  |
| dulwich_log              | 29.8 ms                                                | 35.3 ms: 1.18x slower                                  |
| sympy_sum                | 77.6 ms                                                | 92.2 ms: 1.19x slower                                  |
| logging_simple           | 3.69 us                                                | 4.45 us: 1.21x slower                                  |
| logging_format           | 3.98 us                                                | 4.83 us: 1.21x slower                                  |
| fannkuch                 | 248 ms                                                 | 303 ms: 1.22x slower                                   |
| regex_compile            | 77.9 ms                                                | 95.3 ms: 1.22x slower                                  |
| tomli_loads              | 1.39 sec                                               | 1.71 sec: 1.22x slower                                 |
| create_gc_cycles         | 701 us                                                 | 860 us: 1.23x slower                                   |
| async_tree_cpu_io_mixed  | 526 ms                                                 | 649 ms: 1.24x slower                                   |
| float                    | 55.8 ms                                                | 69.0 ms: 1.24x slower                                  |
| unpack_sequence          | 31.5 ns                                                | 39.0 ns: 1.24x slower                                  |
| spectral_norm            | 76.4 ms                                                | 94.8 ms: 1.24x slower                                  |
| tornado_http             | 69.3 ms                                                | 86.7 ms: 1.25x slower                                  |
| deepcopy_memo            | 27.7 us                                                | 34.7 us: 1.25x slower                                  |
| mako                     | 7.71 ms                                                | 9.87 ms: 1.28x slower                                  |
| pprint_safe_repr         | 497 ms                                                 | 641 ms: 1.29x slower                                   |
| asyncio_tcp_ssl          | 1.24 sec                                               | 1.60 sec: 1.29x slower                                 |
| pprint_pformat           | 1.01 sec                                               | 1.30 sec: 1.29x slower                                 |
| unpickle_pure_python     | 151 us                                                 | 194 us: 1.29x slower                                   |
| pycparser                | 677 ms                                                 | 877 ms: 1.29x slower                                   |
| json_dumps               | 6.22 ms                                                | 8.11 ms: 1.30x slower                                  |
| sqlalchemy_imperative    | 6.68 ms                                                | 8.86 ms: 1.33x slower                                  |
| chameleon                | 4.70 ms                                                | 6.26 ms: 1.33x slower                                  |
| nbody                    | 68.8 ms                                                | 93.0 ms: 1.35x slower                                  |
| pyflate                  | 316 ms                                                 | 427 ms: 1.35x slower                                   |
| scimark_lu               | 76.0 ms                                                | 103 ms: 1.35x slower                                   |
| hexiom                   | 4.54 ms                                                | 6.19 ms: 1.36x slower                                  |
| crypto_pyaes             | 51.9 ms                                                | 71.8 ms: 1.39x slower                                  |
| pickle_pure_python       | 200 us                                                 | 281 us: 1.40x slower                                   |
| sqlglot_transpile        | 1.02 ms                                                | 1.44 ms: 1.41x slower                                  |
| raytrace                 | 212 ms                                                 | 301 ms: 1.42x slower                                   |
| scimark_monte_carlo      | 45.0 ms                                                | 65.6 ms: 1.46x slower                                  |
| async_tree_none          | 266 ms                                                 | 388 ms: 1.46x slower                                   |
| sqlglot_parse            | 848 us                                                 | 1.24 ms: 1.47x slower                                  |
| async_tree_io            | 668 ms                                                 | 980 ms: 1.47x slower                                   |
| scimark_sor              | 87.4 ms                                                | 128 ms: 1.47x slower                                   |
| asyncio_tcp              | 449 ms                                                 | 659 ms: 1.47x slower                                   |
| go                       | 102 ms                                                 | 151 ms: 1.48x slower                                   |
| richards                 | 32.1 ms                                                | 48.7 ms: 1.52x slower                                  |
| async_tree_memoization   | 312 ms                                                 | 474 ms: 1.52x slower                                   |
| logging_silent           | 76.4 ns                                                | 117 ns: 1.53x slower                                   |
| chaos                    | 42.5 ms                                                | 65.8 ms: 1.55x slower                                  |
| mypy2                    | 380 ms                                                 | 607 ms: 1.60x slower                                   |
| richards_super           | 36.0 ms                                                | 57.8 ms: 1.61x slower                                  |
| deltablue                | 2.71 ms                                                | 4.91 ms: 1.81x slower                                  |
| typing_runtime_protocols | 93.0 us                                                | 323 us: 3.47x slower                                   |
| Geometric mean           | (ref)                                                  | 1.19x slower                                           |

Benchmark hidden because not significant (3): json, asyncio_websockets, pathlib
Ignored benchmarks (4) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
Ignored benchmarks (6) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.16x
- 95% likely to have a slowdown of 1.15x
- 99% likely to have a slowdown of 1.13x


# Memory

- memory change: 0.93x