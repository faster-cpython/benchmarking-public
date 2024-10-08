# Results vs. 3.10.4

- fork: python
- ref: 0fb18b02c8ad56299d6a
- machine: linux-aarch64
- commit hash: 0fb18b0
- commit date: 2023-10-02
- overall geometric mean: 1.28x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.25x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 308 ms: 1.24x faster                                                  |
| chameleon      | 10.8 ms                                                               | 8.81 ms: 1.23x faster                                                 |
| docutils       | 3.53 sec                                                              | 2.98 sec: 1.18x faster                                                |
| html5lib       | 86.5 ms                                                               | 65.1 ms: 1.33x faster                                                 |
| tornado_http   | 178 ms                                                                | 136 ms: 1.32x faster                                                  |
| Geometric mean | (ref)                                                                 | 1.26x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 |
|-------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 1.41 sec: 1.62x faster                                                |
| async_tree_none         | 950 ms                                                                | 624 ms: 1.52x faster                                                  |
| async_tree_memoization  | 1.13 sec                                                              | 777 ms: 1.46x faster                                                  |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 912 ms: 1.39x faster                                                  |
| Geometric mean          | (ref)                                                                 | 1.50x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 166 ms                                                                | 105 ms: 1.59x faster                                                  |
| float          | 135 ms                                                                | 92.1 ms: 1.46x faster                                                 |
| pidigits       | 235 ms                                                                | 233 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                                 | 1.33x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 137 ms: 1.29x faster                                                  |
| regex_v8       | 32.2 ms                                                               | 28.3 ms: 1.13x faster                                                 |
| regex_dna      | 257 ms                                                                | 254 ms: 1.01x faster                                                  |
| regex_effbot   | 4.25 ms                                                               | 4.64 ms: 1.09x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.08x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 365 us: 1.45x faster                                                  |
| unpickle_pure_python | 366 us                                                                | 260 us: 1.41x faster                                                  |
| json_dumps           | 16.7 ms                                                               | 12.3 ms: 1.36x faster                                                 |
| tomli_loads          | 3.36 sec                                                              | 2.59 sec: 1.30x faster                                                |
| xml_etree_process    | 99.5 ms                                                               | 79.0 ms: 1.26x faster                                                 |
| unpickle_list        | 6.99 us                                                               | 6.17 us: 1.13x faster                                                 |
| xml_etree_generate   | 123 ms                                                                | 112 ms: 1.10x faster                                                  |
| xml_etree_parse      | 212 ms                                                                | 195 ms: 1.09x faster                                                  |
| xml_etree_iterparse  | 156 ms                                                                | 150 ms: 1.04x faster                                                  |
| json_loads           | 30.9 us                                                               | 30.7 us: 1.01x faster                                                 |
| unpickle             | 17.5 us                                                               | 18.5 us: 1.06x slower                                                 |
| pickle_dict          | 35.1 us                                                               | 37.3 us: 1.06x slower                                                 |
| pickle               | 12.5 us                                                               | 13.4 us: 1.08x slower                                                 |
| Geometric mean       | (ref)                                                                 | 1.13x faster                                                          |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 11.4 ms: 1.02x slower                                                 |
| python_startup_no_site | 6.89 ms                                                               | 8.37 ms: 1.22x slower                                                 |
| Geometric mean         | (ref)                                                                 | 1.11x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 12.9 ms: 1.47x faster                                                 |
| django_template | 53.3 ms                                                               | 40.7 ms: 1.31x faster                                                 |
| genshi_text     | 35.2 ms                                                               | 27.4 ms: 1.28x faster                                                 |
| genshi_xml      | 69.8 ms                                                               | 60.6 ms: 1.15x faster                                                 |
| Geometric mean  | (ref)                                                                 | 1.30x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 181 us: 3.66x faster                                                  |
| deltablue                | 8.94 ms                                                               | 4.12 ms: 2.17x faster                                                 |
| bench_mp_pool            | 14.5 ms                                                               | 7.05 ms: 2.06x faster                                                 |
| richards_super           | 107 ms                                                                | 58.5 ms: 1.83x faster                                                 |
| richards                 | 91.7 ms                                                               | 50.9 ms: 1.80x faster                                                 |
| logging_silent           | 222 ns                                                                | 127 ns: 1.75x faster                                                  |
| chaos                    | 121 ms                                                                | 71.4 ms: 1.70x faster                                                 |
| go                       | 264 ms                                                                | 157 ms: 1.68x faster                                                  |
| asyncio_tcp              | 944 ms                                                                | 566 ms: 1.67x faster                                                  |
| scimark_sor              | 246 ms                                                                | 150 ms: 1.65x faster                                                  |
| sqlglot_parse            | 2.40 ms                                                               | 1.46 ms: 1.64x faster                                                 |
| raytrace                 | 573 ms                                                                | 353 ms: 1.62x faster                                                  |
| async_tree_io            | 2.28 sec                                                              | 1.41 sec: 1.62x faster                                                |
| nbody                    | 166 ms                                                                | 105 ms: 1.59x faster                                                  |
| generators               | 68.1 ms                                                               | 43.5 ms: 1.56x faster                                                 |
| hexiom                   | 10.9 ms                                                               | 6.98 ms: 1.56x faster                                                 |
| scimark_lu               | 227 ms                                                                | 146 ms: 1.56x faster                                                  |
| sqlglot_transpile        | 2.84 ms                                                               | 1.83 ms: 1.55x faster                                                 |
| crypto_pyaes             | 134 ms                                                                | 86.6 ms: 1.55x faster                                                 |
| async_tree_none          | 950 ms                                                                | 624 ms: 1.52x faster                                                  |
| scimark_monte_carlo      | 128 ms                                                                | 85.1 ms: 1.50x faster                                                 |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.19 sec: 1.50x faster                                                |
| mako                     | 18.9 ms                                                               | 12.9 ms: 1.47x faster                                                 |
| float                    | 135 ms                                                                | 92.1 ms: 1.46x faster                                                 |
| async_tree_memoization   | 1.13 sec                                                              | 777 ms: 1.46x faster                                                  |
| pickle_pure_python       | 529 us                                                                | 365 us: 1.45x faster                                                  |
| spectral_norm            | 186 ms                                                                | 131 ms: 1.43x faster                                                  |
| pyflate                  | 795 ms                                                                | 559 ms: 1.42x faster                                                  |
| unpickle_pure_python     | 366 us                                                                | 260 us: 1.41x faster                                                  |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 912 ms: 1.39x faster                                                  |
| pylint                   | 485 ms                                                                | 355 ms: 1.37x faster                                                  |
| json_dumps               | 16.7 ms                                                               | 12.3 ms: 1.36x faster                                                 |
| pycparser                | 1.69 sec                                                              | 1.26 sec: 1.35x faster                                                |
| thrift                   | 1.26 ms                                                               | 937 us: 1.34x faster                                                  |
| html5lib                 | 86.5 ms                                                               | 65.1 ms: 1.33x faster                                                 |
| tornado_http             | 178 ms                                                                | 136 ms: 1.32x faster                                                  |
| django_template          | 53.3 ms                                                               | 40.7 ms: 1.31x faster                                                 |
| comprehensions           | 33.1 us                                                               | 25.4 us: 1.31x faster                                                 |
| tomli_loads              | 3.36 sec                                                              | 2.59 sec: 1.30x faster                                                |
| regex_compile            | 177 ms                                                                | 137 ms: 1.29x faster                                                  |
| genshi_text              | 35.2 ms                                                               | 27.4 ms: 1.28x faster                                                 |
| coroutines               | 37.2 ms                                                               | 29.0 ms: 1.28x faster                                                 |
| logging_simple           | 9.78 us                                                               | 7.63 us: 1.28x faster                                                 |
| gunicorn                 | 1.45 ms                                                               | 1.14 ms: 1.28x faster                                                 |
| logging_format           | 10.6 us                                                               | 8.34 us: 1.27x faster                                                 |
| xml_etree_process        | 99.5 ms                                                               | 79.0 ms: 1.26x faster                                                 |
| sqlalchemy_declarative   | 197 ms                                                                | 157 ms: 1.25x faster                                                  |
| pprint_pformat           | 2.36 sec                                                              | 1.88 sec: 1.25x faster                                                |
| pprint_safe_repr         | 1.15 sec                                                              | 916 ms: 1.25x faster                                                  |
| deepcopy_memo            | 61.7 us                                                               | 49.6 us: 1.24x faster                                                 |
| sqlglot_normalize        | 156 ms                                                                | 126 ms: 1.24x faster                                                  |
| 2to3                     | 381 ms                                                                | 308 ms: 1.24x faster                                                  |
| sqlalchemy_imperative    | 20.5 ms                                                               | 16.7 ms: 1.23x faster                                                 |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.19 ms: 1.23x faster                                                 |
| fannkuch                 | 546 ms                                                                | 443 ms: 1.23x faster                                                  |
| chameleon                | 10.8 ms                                                               | 8.81 ms: 1.23x faster                                                 |
| sqlglot_optimize         | 75.4 ms                                                               | 61.3 ms: 1.23x faster                                                 |
| sympy_integrate          | 26.5 ms                                                               | 21.6 ms: 1.23x faster                                                 |
| bench_thread_pool        | 1.59 ms                                                               | 1.31 ms: 1.22x faster                                                 |
| aiohttp                  | 1.39 ms                                                               | 1.16 ms: 1.20x faster                                                 |
| sympy_expand             | 543 ms                                                                | 454 ms: 1.20x faster                                                  |
| scimark_fft              | 500 ms                                                                | 418 ms: 1.20x faster                                                  |
| dask                     | 450 ms                                                                | 376 ms: 1.19x faster                                                  |
| sympy_sum                | 184 ms                                                                | 154 ms: 1.19x faster                                                  |
| dulwich_log              | 73.5 ms                                                               | 62.0 ms: 1.19x faster                                                 |
| nqueens                  | 117 ms                                                                | 99.2 ms: 1.18x faster                                                 |
| docutils                 | 3.53 sec                                                              | 2.98 sec: 1.18x faster                                                |
| create_gc_cycles         | 2.26 ms                                                               | 1.92 ms: 1.18x faster                                                 |
| sympy_str                | 329 ms                                                                | 280 ms: 1.18x faster                                                  |
| genshi_xml               | 69.8 ms                                                               | 60.6 ms: 1.15x faster                                                 |
| deepcopy                 | 511 us                                                                | 446 us: 1.15x faster                                                  |
| regex_v8                 | 32.2 ms                                                               | 28.3 ms: 1.13x faster                                                 |
| unpickle_list            | 6.99 us                                                               | 6.17 us: 1.13x faster                                                 |
| meteor_contest           | 126 ms                                                                | 112 ms: 1.13x faster                                                  |
| deepcopy_reduce          | 4.60 us                                                               | 4.10 us: 1.12x faster                                                 |
| xml_etree_generate       | 123 ms                                                                | 112 ms: 1.10x faster                                                  |
| sqlite_synth             | 4.12 us                                                               | 3.77 us: 1.09x faster                                                 |
| xml_etree_parse          | 212 ms                                                                | 195 ms: 1.09x faster                                                  |
| mdp                      | 3.70 sec                                                              | 3.41 sec: 1.08x faster                                                |
| pathlib                  | 26.3 ms                                                               | 24.5 ms: 1.07x faster                                                 |
| mypy2                    | 936 ms                                                                | 873 ms: 1.07x faster                                                  |
| json                     | 5.88 ms                                                               | 5.54 ms: 1.06x faster                                                 |
| xml_etree_iterparse      | 156 ms                                                                | 150 ms: 1.04x faster                                                  |
| regex_dna                | 257 ms                                                                | 254 ms: 1.01x faster                                                  |
| pidigits                 | 235 ms                                                                | 233 ms: 1.01x faster                                                  |
| json_loads               | 30.9 us                                                               | 30.7 us: 1.01x faster                                                 |
| telco                    | 8.49 ms                                                               | 8.51 ms: 1.00x slower                                                 |
| python_startup           | 11.2 ms                                                               | 11.4 ms: 1.02x slower                                                 |
| coverage                 | 83.6 ms                                                               | 87.3 ms: 1.04x slower                                                 |
| unpickle                 | 17.5 us                                                               | 18.5 us: 1.06x slower                                                 |
| gc_traversal             | 4.15 ms                                                               | 4.40 ms: 1.06x slower                                                 |
| pickle_dict              | 35.1 us                                                               | 37.3 us: 1.06x slower                                                 |
| pickle                   | 12.5 us                                                               | 13.4 us: 1.08x slower                                                 |
| async_generators         | 452 ms                                                                | 491 ms: 1.08x slower                                                  |
| regex_effbot             | 4.25 ms                                                               | 4.64 ms: 1.09x slower                                                 |
| python_startup_no_site   | 6.89 ms                                                               | 8.37 ms: 1.22x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.28x faster                                                          |

Benchmark hidden because not significant (2): asyncio_websockets, pickle_list
Ignored benchmarks (1) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: flaskblogging
Ignored benchmarks (4) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.25x