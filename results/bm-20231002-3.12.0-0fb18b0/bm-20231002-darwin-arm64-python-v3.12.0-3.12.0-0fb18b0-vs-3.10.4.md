
# Results vs. 3.10.4

- fork: python
- ref: v3.12.0
- machine: darwin-arm64
- commit hash: 0fb18b0
- commit date: 2023-10-02
- overall geometric mean: 1.19x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 169 ms: 1.13x faster                                   |
| chameleon      | 6.26 ms                                                | 4.70 ms: 1.33x faster                                  |
| docutils       | 1.73 sec                                               | 1.50 sec: 1.15x faster                                 |
| tornado_http   | 86.7 ms                                                | 69.3 ms: 1.25x faster                                  |
| Geometric mean | (ref)                                                  | 1.21x faster                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| async_tree_memoization  | 474 ms                                                 | 312 ms: 1.52x faster                                   |
| async_tree_io           | 980 ms                                                 | 668 ms: 1.47x faster                                   |
| async_tree_none         | 388 ms                                                 | 266 ms: 1.46x faster                                   |
| async_tree_cpu_io_mixed | 649 ms                                                 | 526 ms: 1.24x faster                                   |
| Geometric mean          | (ref)                                                  | 1.42x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 68.8 ms: 1.35x faster                                  |
| float          | 69.0 ms                                                | 55.8 ms: 1.24x faster                                  |
| pidigits       | 282 ms                                                 | 282 ms: 1.00x faster                                   |
| Geometric mean | (ref)                                                  | 1.19x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 77.9 ms: 1.22x faster                                  |
| regex_dna      | 174 ms                                                 | 154 ms: 1.13x faster                                   |
| regex_v8       | 17.1 ms                                                | 16.0 ms: 1.07x faster                                  |
| regex_effbot   | 2.46 ms                                                | 2.64 ms: 1.07x slower                                  |
| Geometric mean | (ref)                                                  | 1.08x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 200 us: 1.40x faster                                   |
| json_dumps           | 8.11 ms                                                | 6.22 ms: 1.30x faster                                  |
| unpickle_pure_python | 194 us                                                 | 151 us: 1.29x faster                                   |
| tomli_loads          | 1.71 sec                                               | 1.39 sec: 1.22x faster                                 |
| xml_etree_process    | 46.5 ms                                                | 39.7 ms: 1.17x faster                                  |
| xml_etree_parse      | 108 ms                                                 | 106 ms: 1.01x faster                                   |
| xml_etree_iterparse  | 72.1 ms                                                | 74.0 ms: 1.03x slower                                  |
| pickle               | 6.97 us                                                | 7.23 us: 1.04x slower                                  |
| unpickle             | 8.80 us                                                | 9.12 us: 1.04x slower                                  |
| xml_etree_generate   | 53.5 ms                                                | 55.8 ms: 1.04x slower                                  |
| json_loads           | 16.4 us                                                | 17.2 us: 1.05x slower                                  |
| pickle_list          | 2.74 us                                                | 2.89 us: 1.05x slower                                  |
| pickle_dict          | 17.0 us                                                | 18.1 us: 1.06x slower                                  |
| unpickle_list        | 2.69 us                                                | 3.02 us: 1.12x slower                                  |
| Geometric mean       | (ref)                                                  | 1.06x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 11.4 ms: 1.05x slower                                  |
| python_startup_no_site | 7.91 ms                                                | 9.37 ms: 1.19x slower                                  |
| Geometric mean         | (ref)                                                  | 1.12x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 9.87 ms                                                | 7.71 ms: 1.28x faster                                  |
| django_template | 26.4 ms                                                | 22.3 ms: 1.18x faster                                  |
| Geometric mean  | (ref)                                                  | 1.23x faster                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 93.0 us: 3.47x faster                                  |
| deltablue                | 4.91 ms                                                | 2.71 ms: 1.81x faster                                  |
| richards_super           | 57.8 ms                                                | 36.0 ms: 1.61x faster                                  |
| mypy2                    | 607 ms                                                 | 380 ms: 1.60x faster                                   |
| chaos                    | 65.8 ms                                                | 42.5 ms: 1.55x faster                                  |
| logging_silent           | 117 ns                                                 | 76.4 ns: 1.53x faster                                  |
| async_tree_memoization   | 474 ms                                                 | 312 ms: 1.52x faster                                   |
| richards                 | 48.7 ms                                                | 32.1 ms: 1.52x faster                                  |
| go                       | 151 ms                                                 | 102 ms: 1.48x faster                                   |
| asyncio_tcp              | 659 ms                                                 | 449 ms: 1.47x faster                                   |
| scimark_sor              | 128 ms                                                 | 87.4 ms: 1.47x faster                                  |
| async_tree_io            | 980 ms                                                 | 668 ms: 1.47x faster                                   |
| sqlglot_parse            | 1.24 ms                                                | 848 us: 1.47x faster                                   |
| async_tree_none          | 388 ms                                                 | 266 ms: 1.46x faster                                   |
| scimark_monte_carlo      | 65.6 ms                                                | 45.0 ms: 1.46x faster                                  |
| raytrace                 | 301 ms                                                 | 212 ms: 1.42x faster                                   |
| sqlglot_transpile        | 1.44 ms                                                | 1.02 ms: 1.41x faster                                  |
| pickle_pure_python       | 281 us                                                 | 200 us: 1.40x faster                                   |
| crypto_pyaes             | 71.8 ms                                                | 51.9 ms: 1.39x faster                                  |
| hexiom                   | 6.19 ms                                                | 4.54 ms: 1.36x faster                                  |
| scimark_lu               | 103 ms                                                 | 76.0 ms: 1.35x faster                                  |
| pyflate                  | 427 ms                                                 | 316 ms: 1.35x faster                                   |
| nbody                    | 93.0 ms                                                | 68.8 ms: 1.35x faster                                  |
| chameleon                | 6.26 ms                                                | 4.70 ms: 1.33x faster                                  |
| sqlalchemy_imperative    | 8.86 ms                                                | 6.68 ms: 1.33x faster                                  |
| json_dumps               | 8.11 ms                                                | 6.22 ms: 1.30x faster                                  |
| pycparser                | 877 ms                                                 | 677 ms: 1.29x faster                                   |
| unpickle_pure_python     | 194 us                                                 | 151 us: 1.29x faster                                   |
| pprint_pformat           | 1.30 sec                                               | 1.01 sec: 1.29x faster                                 |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.24 sec: 1.29x faster                                 |
| pprint_safe_repr         | 641 ms                                                 | 497 ms: 1.29x faster                                   |
| mako                     | 9.87 ms                                                | 7.71 ms: 1.28x faster                                  |
| deepcopy_memo            | 34.7 us                                                | 27.7 us: 1.25x faster                                  |
| tornado_http             | 86.7 ms                                                | 69.3 ms: 1.25x faster                                  |
| spectral_norm            | 94.8 ms                                                | 76.4 ms: 1.24x faster                                  |
| unpack_sequence          | 39.0 ns                                                | 31.5 ns: 1.24x faster                                  |
| float                    | 69.0 ms                                                | 55.8 ms: 1.24x faster                                  |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 526 ms: 1.24x faster                                   |
| create_gc_cycles         | 860 us                                                 | 701 us: 1.23x faster                                   |
| tomli_loads              | 1.71 sec                                               | 1.39 sec: 1.22x faster                                 |
| regex_compile            | 95.3 ms                                                | 77.9 ms: 1.22x faster                                  |
| fannkuch                 | 303 ms                                                 | 248 ms: 1.22x faster                                   |
| logging_format           | 4.83 us                                                | 3.98 us: 1.21x faster                                  |
| logging_simple           | 4.45 us                                                | 3.69 us: 1.21x faster                                  |
| sympy_sum                | 92.2 ms                                                | 77.6 ms: 1.19x faster                                  |
| dulwich_log              | 35.3 ms                                                | 29.8 ms: 1.18x faster                                  |
| django_template          | 26.4 ms                                                | 22.3 ms: 1.18x faster                                  |
| sqlalchemy_declarative   | 73.3 ms                                                | 62.3 ms: 1.18x faster                                  |
| xml_etree_process        | 46.5 ms                                                | 39.7 ms: 1.17x faster                                  |
| comprehensions           | 16.9 us                                                | 14.5 us: 1.16x faster                                  |
| deepcopy                 | 272 us                                                 | 235 us: 1.16x faster                                   |
| sympy_integrate          | 13.1 ms                                                | 11.4 ms: 1.16x faster                                  |
| docutils                 | 1.73 sec                                               | 1.50 sec: 1.15x faster                                 |
| scimark_fft              | 224 ms                                                 | 195 ms: 1.15x faster                                   |
| dask                     | 253 ms                                                 | 222 ms: 1.14x faster                                   |
| gunicorn                 | 1.30 ms                                                | 1.15 ms: 1.14x faster                                  |
| aiohttp                  | 1.22 ms                                                | 1.08 ms: 1.13x faster                                  |
| 2to3                     | 192 ms                                                 | 169 ms: 1.13x faster                                   |
| regex_dna                | 174 ms                                                 | 154 ms: 1.13x faster                                   |
| deepcopy_reduce          | 2.33 us                                                | 2.07 us: 1.13x faster                                  |
| sympy_str                | 165 ms                                                 | 148 ms: 1.12x faster                                   |
| sympy_expand             | 269 ms                                                 | 241 ms: 1.12x faster                                   |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 3.14 ms: 1.09x faster                                  |
| meteor_contest           | 77.7 ms                                                | 71.7 ms: 1.08x faster                                  |
| sqlglot_optimize         | 36.8 ms                                                | 34.0 ms: 1.08x faster                                  |
| coroutines               | 20.7 ms                                                | 19.2 ms: 1.08x faster                                  |
| regex_v8                 | 17.1 ms                                                | 16.0 ms: 1.07x faster                                  |
| coverage                 | 41.5 ms                                                | 38.9 ms: 1.07x faster                                  |
| bench_thread_pool        | 527 us                                                 | 504 us: 1.05x faster                                   |
| generators               | 32.3 ms                                                | 31.1 ms: 1.04x faster                                  |
| mdp                      | 1.63 sec                                               | 1.58 sec: 1.03x faster                                 |
| sqlglot_normalize        | 190 ms                                                 | 186 ms: 1.02x faster                                   |
| nqueens                  | 63.8 ms                                                | 62.4 ms: 1.02x faster                                  |
| xml_etree_parse          | 108 ms                                                 | 106 ms: 1.01x faster                                   |
| pidigits                 | 282 ms                                                 | 282 ms: 1.00x faster                                   |
| gc_traversal             | 2.36 ms                                                | 2.40 ms: 1.02x slower                                  |
| xml_etree_iterparse      | 72.1 ms                                                | 74.0 ms: 1.03x slower                                  |
| pickle                   | 6.97 us                                                | 7.23 us: 1.04x slower                                  |
| unpickle                 | 8.80 us                                                | 9.12 us: 1.04x slower                                  |
| xml_etree_generate       | 53.5 ms                                                | 55.8 ms: 1.04x slower                                  |
| json_loads               | 16.4 us                                                | 17.2 us: 1.05x slower                                  |
| python_startup           | 10.9 ms                                                | 11.4 ms: 1.05x slower                                  |
| pickle_list              | 2.74 us                                                | 2.89 us: 1.05x slower                                  |
| telco                    | 3.49 ms                                                | 3.68 ms: 1.05x slower                                  |
| pickle_dict              | 17.0 us                                                | 18.1 us: 1.06x slower                                  |
| regex_effbot             | 2.46 ms                                                | 2.64 ms: 1.07x slower                                  |
| sqlite_synth             | 1.46 us                                                | 1.57 us: 1.08x slower                                  |
| unpickle_list            | 2.69 us                                                | 3.02 us: 1.12x slower                                  |
| python_startup_no_site   | 7.91 ms                                                | 9.37 ms: 1.19x slower                                  |
| bench_mp_pool            | 37.4 ms                                                | 44.9 ms: 1.20x slower                                  |
| async_generators         | 231 ms                                                 | 304 ms: 1.31x slower                                   |
| Geometric mean           | (ref)                                                  | 1.19x faster                                           |

Benchmark hidden because not significant (3): pathlib, asyncio_websockets, json
Ignored benchmarks (6) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
Ignored benchmarks (4) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.16x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.13x


# Memory

- memory change: 1.11x