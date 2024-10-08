# Results vs. 3.10.4

- fork: python
- ref: v3.13.0a4
- machine: darwin-arm64
- commit hash: 9d34f60
- commit date: 2024-02-15
- overall geometric mean: 1.18x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: 1.26x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 190 ms: 1.01x faster                                       |
| chameleon      | 6.26 ms                                                | 4.81 ms: 1.30x faster                                      |
| docutils       | 1.73 sec                                               | 1.48 sec: 1.17x faster                                     |
| tornado_http   | 86.7 ms                                                | 69.6 ms: 1.25x faster                                      |
| Geometric mean | (ref)                                                  | 1.18x faster                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 252 ms: 1.54x faster                                       |
| async_tree_memoization  | 474 ms                                                 | 328 ms: 1.45x faster                                       |
| async_tree_io           | 980 ms                                                 | 699 ms: 1.40x faster                                       |
| async_tree_cpu_io_mixed | 649 ms                                                 | 519 ms: 1.25x faster                                       |
| Geometric mean          | (ref)                                                  | 1.41x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| float          | 69.0 ms                                                | 55.5 ms: 1.24x faster                                      |
| nbody          | 93.0 ms                                                | 75.9 ms: 1.23x faster                                      |
| Geometric mean | (ref)                                                  | 1.15x faster                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 75.1 ms: 1.27x faster                                      |
| regex_dna      | 174 ms                                                 | 150 ms: 1.16x faster                                       |
| regex_v8       | 17.1 ms                                                | 17.4 ms: 1.01x slower                                      |
| regex_effbot   | 2.46 ms                                                | 2.54 ms: 1.03x slower                                      |
| Geometric mean | (ref)                                                  | 1.09x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 196 us: 1.43x faster                                       |
| json_dumps           | 8.11 ms                                                | 6.48 ms: 1.25x faster                                      |
| unpickle_pure_python | 194 us                                                 | 158 us: 1.23x faster                                       |
| tomli_loads          | 1.71 sec                                               | 1.40 sec: 1.22x faster                                     |
| xml_etree_process    | 46.5 ms                                                | 38.7 ms: 1.20x faster                                      |
| xml_etree_parse      | 108 ms                                                 | 105 ms: 1.02x faster                                       |
| json_loads           | 16.4 us                                                | 16.9 us: 1.03x slower                                      |
| xml_etree_iterparse  | 72.1 ms                                                | 74.8 ms: 1.04x slower                                      |
| unpickle             | 8.80 us                                                | 9.18 us: 1.04x slower                                      |
| xml_etree_generate   | 53.5 ms                                                | 56.1 ms: 1.05x slower                                      |
| pickle               | 6.97 us                                                | 7.33 us: 1.05x slower                                      |
| pickle_dict          | 17.0 us                                                | 18.2 us: 1.07x slower                                      |
| pickle_list          | 2.74 us                                                | 2.99 us: 1.09x slower                                      |
| unpickle_list        | 2.69 us                                                | 3.10 us: 1.15x slower                                      |
| Geometric mean       | (ref)                                                  | 1.05x faster                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 13.1 ms: 1.20x slower                                      |
| python_startup_no_site | 7.91 ms                                                | 11.6 ms: 1.46x slower                                      |
| Geometric mean         | (ref)                                                  | 1.33x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|-----------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako      | 9.87 ms                                                | 7.79 ms: 1.27x faster                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 70.9 us: 4.56x faster                                      |
| deltablue                | 4.91 ms                                                | 2.45 ms: 2.00x faster                                      |
| raytrace                 | 301 ms                                                 | 176 ms: 1.71x faster                                       |
| logging_silent           | 117 ns                                                 | 70.3 ns: 1.67x faster                                      |
| asyncio_tcp              | 659 ms                                                 | 401 ms: 1.64x faster                                       |
| richards_super           | 57.8 ms                                                | 35.7 ms: 1.62x faster                                      |
| chaos                    | 65.8 ms                                                | 41.0 ms: 1.60x faster                                      |
| sqlglot_parse            | 1.24 ms                                                | 787 us: 1.58x faster                                       |
| async_tree_none          | 388 ms                                                 | 252 ms: 1.54x faster                                       |
| richards                 | 48.7 ms                                                | 31.9 ms: 1.53x faster                                      |
| sqlglot_transpile        | 1.44 ms                                                | 973 us: 1.48x faster                                       |
| crypto_pyaes             | 71.8 ms                                                | 49.1 ms: 1.46x faster                                      |
| async_tree_memoization   | 474 ms                                                 | 328 ms: 1.45x faster                                       |
| pickle_pure_python       | 281 us                                                 | 196 us: 1.43x faster                                       |
| async_tree_io            | 980 ms                                                 | 699 ms: 1.40x faster                                       |
| scimark_lu               | 103 ms                                                 | 74.8 ms: 1.37x faster                                      |
| unpack_sequence          | 39.0 ns                                                | 28.4 ns: 1.37x faster                                      |
| go                       | 151 ms                                                 | 110 ms: 1.37x faster                                       |
| scimark_monte_carlo      | 65.6 ms                                                | 48.5 ms: 1.35x faster                                      |
| comprehensions           | 16.9 us                                                | 12.6 us: 1.35x faster                                      |
| deepcopy_memo            | 34.7 us                                                | 26.3 us: 1.32x faster                                      |
| pyflate                  | 427 ms                                                 | 326 ms: 1.31x faster                                       |
| chameleon                | 6.26 ms                                                | 4.81 ms: 1.30x faster                                      |
| logging_simple           | 4.45 us                                                | 3.45 us: 1.29x faster                                      |
| logging_format           | 4.83 us                                                | 3.76 us: 1.29x faster                                      |
| regex_compile            | 95.3 ms                                                | 75.1 ms: 1.27x faster                                      |
| mako                     | 9.87 ms                                                | 7.79 ms: 1.27x faster                                      |
| pycparser                | 877 ms                                                 | 693 ms: 1.26x faster                                       |
| hexiom                   | 6.19 ms                                                | 4.91 ms: 1.26x faster                                      |
| json_dumps               | 8.11 ms                                                | 6.48 ms: 1.25x faster                                      |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 519 ms: 1.25x faster                                       |
| tornado_http             | 86.7 ms                                                | 69.6 ms: 1.25x faster                                      |
| pprint_pformat           | 1.30 sec                                               | 1.05 sec: 1.24x faster                                     |
| pprint_safe_repr         | 641 ms                                                 | 515 ms: 1.24x faster                                       |
| float                    | 69.0 ms                                                | 55.5 ms: 1.24x faster                                      |
| unpickle_pure_python     | 194 us                                                 | 158 us: 1.23x faster                                       |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.31 sec: 1.23x faster                                     |
| nbody                    | 93.0 ms                                                | 75.9 ms: 1.23x faster                                      |
| sympy_sum                | 92.2 ms                                                | 75.3 ms: 1.22x faster                                      |
| create_gc_cycles         | 860 us                                                 | 705 us: 1.22x faster                                       |
| tomli_loads              | 1.71 sec                                               | 1.40 sec: 1.22x faster                                     |
| scimark_sor              | 128 ms                                                 | 106 ms: 1.21x faster                                       |
| spectral_norm            | 94.8 ms                                                | 78.8 ms: 1.20x faster                                      |
| deepcopy                 | 272 us                                                 | 226 us: 1.20x faster                                       |
| xml_etree_process        | 46.5 ms                                                | 38.7 ms: 1.20x faster                                      |
| sympy_integrate          | 13.1 ms                                                | 11.1 ms: 1.19x faster                                      |
| dulwich_log              | 35.3 ms                                                | 29.8 ms: 1.18x faster                                      |
| deepcopy_reduce          | 2.33 us                                                | 1.98 us: 1.17x faster                                      |
| sympy_str                | 165 ms                                                 | 141 ms: 1.17x faster                                       |
| docutils                 | 1.73 sec                                               | 1.48 sec: 1.17x faster                                     |
| regex_dna                | 174 ms                                                 | 150 ms: 1.16x faster                                       |
| generators               | 32.3 ms                                                | 28.3 ms: 1.14x faster                                      |
| fannkuch                 | 303 ms                                                 | 267 ms: 1.13x faster                                       |
| sympy_expand             | 269 ms                                                 | 241 ms: 1.12x faster                                       |
| coroutines               | 20.7 ms                                                | 18.7 ms: 1.10x faster                                      |
| sqlglot_optimize         | 36.8 ms                                                | 34.4 ms: 1.07x faster                                      |
| scimark_fft              | 224 ms                                                 | 213 ms: 1.05x faster                                       |
| bench_thread_pool        | 527 us                                                 | 504 us: 1.05x faster                                       |
| json                     | 3.08 ms                                                | 2.95 ms: 1.05x faster                                      |
| meteor_contest           | 77.7 ms                                                | 74.3 ms: 1.05x faster                                      |
| sqlglot_normalize        | 190 ms                                                 | 182 ms: 1.04x faster                                       |
| nqueens                  | 63.8 ms                                                | 61.6 ms: 1.04x faster                                      |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 3.31 ms: 1.03x faster                                      |
| xml_etree_parse          | 108 ms                                                 | 105 ms: 1.02x faster                                       |
| mdp                      | 1.63 sec                                               | 1.61 sec: 1.01x faster                                     |
| 2to3                     | 192 ms                                                 | 190 ms: 1.01x faster                                       |
| gc_traversal             | 2.36 ms                                                | 2.39 ms: 1.01x slower                                      |
| regex_v8                 | 17.1 ms                                                | 17.4 ms: 1.01x slower                                      |
| json_loads               | 16.4 us                                                | 16.9 us: 1.03x slower                                      |
| regex_effbot             | 2.46 ms                                                | 2.54 ms: 1.03x slower                                      |
| pathlib                  | 24.5 ms                                                | 25.4 ms: 1.04x slower                                      |
| xml_etree_iterparse      | 72.1 ms                                                | 74.8 ms: 1.04x slower                                      |
| unpickle                 | 8.80 us                                                | 9.18 us: 1.04x slower                                      |
| xml_etree_generate       | 53.5 ms                                                | 56.1 ms: 1.05x slower                                      |
| pickle                   | 6.97 us                                                | 7.33 us: 1.05x slower                                      |
| pickle_dict              | 17.0 us                                                | 18.2 us: 1.07x slower                                      |
| pickle_list              | 2.74 us                                                | 2.99 us: 1.09x slower                                      |
| sqlite_synth             | 1.46 us                                                | 1.59 us: 1.09x slower                                      |
| coverage                 | 41.5 ms                                                | 47.5 ms: 1.15x slower                                      |
| unpickle_list            | 2.69 us                                                | 3.10 us: 1.15x slower                                      |
| python_startup           | 10.9 ms                                                | 13.1 ms: 1.20x slower                                      |
| bench_mp_pool            | 37.4 ms                                                | 45.9 ms: 1.23x slower                                      |
| telco                    | 3.49 ms                                                | 4.51 ms: 1.29x slower                                      |
| async_generators         | 231 ms                                                 | 303 ms: 1.31x slower                                       |
| dask                     | 253 ms                                                 | 335 ms: 1.32x slower                                       |
| python_startup_no_site   | 7.91 ms                                                | 11.6 ms: 1.46x slower                                      |
| Geometric mean           | (ref)                                                  | 1.18x faster                                               |

Benchmark hidden because not significant (3): mypy2, asyncio_websockets, pidigits
Ignored benchmarks (11) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, thrift
Ignored benchmarks (4) of results/bm-20240215-3.13.0a4-9d34f60-JIT/bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.15x
- 95% likely to have a speedup of 1.13x
- 99% likely to have a speedup of 1.10x


# Memory

- memory change: 1.26x