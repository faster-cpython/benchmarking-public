# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_ghccc
- machine: linux-x86_64
- commit hash: 98575b4
- commit date: 2024-03-21
- overall geometric mean: 1.14x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240321-linux-x86_64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 303 ms: 1.15x faster                                                 |
| chameleon      | 9.68 ms                                                | 7.04 ms: 1.38x faster                                                |
| docutils       | 3.30 sec                                               | 4.82 sec: 1.46x slower                                               |
| html5lib       | 88.9 ms                                                | 75.2 ms: 1.18x faster                                                |
| tornado_http   | 136 ms                                                 | 101 ms: 1.35x faster                                                 |
| Geometric mean | (ref)                                                  | 1.12x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240321-linux-x86_64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 1.02 sec                                               | 4.17 sec: 4.11x slower                                               |
| async_tree_none         | 728 ms                                                 | 3.43 sec: 4.71x slower                                               |
| async_tree_memoization  | 870 ms                                                 | 4.43 sec: 5.09x slower                                               |
| async_tree_io           | 1.77 sec                                               | 13.3 sec: 7.50x slower                                               |
| Geometric mean          | (ref)                                                  | 5.21x slower                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240321-linux-x86_64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 81.4 ms: 1.89x faster                                                |
| pidigits       | 191 ms                                                 | 189 ms: 1.01x faster                                                 |
| float          | 117 ms                                                 | 139 ms: 1.19x slower                                                 |
| Geometric mean | (ref)                                                  | 1.17x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240321-linux-x86_64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 142 ms: 1.33x faster                                                 |
| regex_v8       | 27.8 ms                                                | 26.1 ms: 1.07x faster                                                |
| regex_effbot   | 3.63 ms                                                | 3.70 ms: 1.02x slower                                                |
| Geometric mean | (ref)                                                  | 1.09x faster                                                         |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240321-linux-x86_64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 307 us: 1.58x faster                                                 |
| tomli_loads          | 3.14 sec                                               | 2.00 sec: 1.57x faster                                               |
| unpickle_pure_python | 331 us                                                 | 227 us: 1.46x faster                                                 |
| json_dumps           | 14.2 ms                                                | 10.6 ms: 1.33x faster                                                |
| xml_etree_process    | 79.1 ms                                                | 68.3 ms: 1.16x faster                                                |
| json_loads           | 31.2 us                                                | 28.4 us: 1.10x faster                                                |
| pickle_list          | 5.08 us                                                | 5.20 us: 1.02x slower                                                |
| unpickle             | 14.4 us                                                | 15.1 us: 1.05x slower                                                |
| pickle               | 10.7 us                                                | 12.0 us: 1.13x slower                                                |
| pickle_dict          | 29.6 us                                                | 36.3 us: 1.23x slower                                                |
| xml_etree_parse      | 168 ms                                                 | 219 ms: 1.30x slower                                                 |
| xml_etree_iterparse  | 115 ms                                                 | 162 ms: 1.40x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                         |

Benchmark hidden because not significant (2): unpickle_list, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240321-linux-x86_64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 11.8 ms: 1.24x faster                                                |
| python_startup_no_site | 5.93 ms                                                | 10.1 ms: 1.70x slower                                                |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240321-linux-x86_64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.4 ms: 1.57x faster                                                |
| django_template | 48.2 ms                                                | 35.5 ms: 1.36x faster                                                |
| genshi_text     | 31.8 ms                                                | 25.1 ms: 1.27x faster                                                |
| genshi_xml      | 66.0 ms                                                | 60.5 ms: 1.09x faster                                                |
| Geometric mean  | (ref)                                                  | 1.31x faster                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240321-linux-x86_64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 113 us: 4.82x faster                                                 |
| generators               | 80.1 ms                                                | 29.7 ms: 2.69x faster                                                |
| deltablue                | 7.91 ms                                                | 3.64 ms: 2.17x faster                                                |
| nbody                    | 154 ms                                                 | 81.4 ms: 1.89x faster                                                |
| logging_silent           | 190 ns                                                 | 101 ns: 1.88x faster                                                 |
| chaos                    | 115 ms                                                 | 61.6 ms: 1.87x faster                                                |
| crypto_pyaes             | 128 ms                                                 | 69.0 ms: 1.85x faster                                                |
| richards_super           | 94.7 ms                                                | 51.7 ms: 1.83x faster                                                |
| scimark_monte_carlo      | 118 ms                                                 | 65.2 ms: 1.81x faster                                                |
| asyncio_tcp              | 922 ms                                                 | 510 ms: 1.81x faster                                                 |
| raytrace                 | 507 ms                                                 | 283 ms: 1.79x faster                                                 |
| richards                 | 79.3 ms                                                | 45.0 ms: 1.76x faster                                                |
| comprehensions           | 28.8 us                                                | 16.9 us: 1.70x faster                                                |
| spectral_norm            | 170 ms                                                 | 100 ms: 1.70x faster                                                 |
| scimark_sor              | 220 ms                                                 | 132 ms: 1.67x faster                                                 |
| pickle_pure_python       | 484 us                                                 | 307 us: 1.58x faster                                                 |
| tomli_loads              | 3.14 sec                                               | 2.00 sec: 1.57x faster                                               |
| mako                     | 16.3 ms                                                | 10.4 ms: 1.57x faster                                                |
| pyflate                  | 716 ms                                                 | 456 ms: 1.57x faster                                                 |
| hexiom                   | 10.4 ms                                                | 6.79 ms: 1.53x faster                                                |
| deepcopy_memo            | 58.5 us                                                | 38.6 us: 1.52x faster                                                |
| go                       | 240 ms                                                 | 159 ms: 1.51x faster                                                 |
| coroutines               | 35.1 ms                                                | 23.3 ms: 1.51x faster                                                |
| sqlglot_parse            | 2.17 ms                                                | 1.45 ms: 1.49x faster                                                |
| scimark_fft              | 466 ms                                                 | 316 ms: 1.48x faster                                                 |
| unpickle_pure_python     | 331 us                                                 | 227 us: 1.46x faster                                                 |
| fannkuch                 | 532 ms                                                 | 373 ms: 1.43x faster                                                 |
| logging_simple           | 8.30 us                                                | 5.84 us: 1.42x faster                                                |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.61 ms: 1.40x faster                                                |
| pprint_safe_repr         | 1.02 sec                                               | 726 ms: 1.40x faster                                                 |
| logging_format           | 9.09 us                                                | 6.49 us: 1.40x faster                                                |
| sqlglot_transpile        | 2.57 ms                                                | 1.84 ms: 1.40x faster                                                |
| pprint_pformat           | 2.10 sec                                               | 1.50 sec: 1.40x faster                                               |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.86 sec: 1.39x faster                                               |
| scimark_lu               | 176 ms                                                 | 127 ms: 1.39x faster                                                 |
| chameleon                | 9.68 ms                                                | 7.04 ms: 1.38x faster                                                |
| django_template          | 48.2 ms                                                | 35.5 ms: 1.36x faster                                                |
| deepcopy                 | 479 us                                                 | 354 us: 1.35x faster                                                 |
| tornado_http             | 136 ms                                                 | 101 ms: 1.35x faster                                                 |
| deepcopy_reduce          | 4.17 us                                                | 3.12 us: 1.33x faster                                                |
| json_dumps               | 14.2 ms                                                | 10.6 ms: 1.33x faster                                                |
| regex_compile            | 188 ms                                                 | 142 ms: 1.33x faster                                                 |
| thrift                   | 1.07 ms                                                | 816 us: 1.31x faster                                                 |
| sqlglot_normalize        | 143 ms                                                 | 113 ms: 1.27x faster                                                 |
| genshi_text              | 31.8 ms                                                | 25.1 ms: 1.27x faster                                                |
| python_startup           | 14.6 ms                                                | 11.8 ms: 1.24x faster                                                |
| sympy_sum                | 196 ms                                                 | 162 ms: 1.22x faster                                                 |
| sympy_integrate          | 25.8 ms                                                | 21.3 ms: 1.21x faster                                                |
| sympy_str                | 346 ms                                                 | 286 ms: 1.21x faster                                                 |
| dulwich_log              | 84.3 ms                                                | 71.0 ms: 1.19x faster                                                |
| nqueens                  | 106 ms                                                 | 89.4 ms: 1.18x faster                                                |
| html5lib                 | 88.9 ms                                                | 75.2 ms: 1.18x faster                                                |
| sqlglot_optimize         | 69.2 ms                                                | 59.1 ms: 1.17x faster                                                |
| sympy_expand             | 566 ms                                                 | 487 ms: 1.16x faster                                                 |
| xml_etree_process        | 79.1 ms                                                | 68.3 ms: 1.16x faster                                                |
| bench_thread_pool        | 986 us                                                 | 856 us: 1.15x faster                                                 |
| 2to3                     | 348 ms                                                 | 303 ms: 1.15x faster                                                 |
| djangocms                | 38.4 us                                                | 33.6 us: 1.14x faster                                                |
| aiohttp                  | 1.44 ms                                                | 1.26 ms: 1.14x faster                                                |
| gunicorn                 | 1.53 ms                                                | 1.35 ms: 1.13x faster                                                |
| json_loads               | 31.2 us                                                | 28.4 us: 1.10x faster                                                |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.09x faster                                                 |
| genshi_xml               | 66.0 ms                                                | 60.5 ms: 1.09x faster                                                |
| create_gc_cycles         | 1.62 ms                                                | 1.49 ms: 1.09x faster                                                |
| json                     | 5.69 ms                                                | 5.22 ms: 1.09x faster                                                |
| pathlib                  | 20.5 ms                                                | 18.8 ms: 1.09x faster                                                |
| sqlite_synth             | 3.02 us                                                | 2.83 us: 1.07x faster                                                |
| regex_v8                 | 27.8 ms                                                | 26.1 ms: 1.07x faster                                                |
| mdp                      | 2.85 sec                                               | 2.70 sec: 1.06x faster                                               |
| mypy2                    | 894 ms                                                 | 852 ms: 1.05x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.51 sec: 1.05x faster                                               |
| pidigits                 | 191 ms                                                 | 189 ms: 1.01x faster                                                 |
| asyncio_websockets       | 559 ms                                                 | 567 ms: 1.01x slower                                                 |
| regex_effbot             | 3.63 ms                                                | 3.70 ms: 1.02x slower                                                |
| pickle_list              | 5.08 us                                                | 5.20 us: 1.02x slower                                                |
| gc_traversal             | 3.62 ms                                                | 3.75 ms: 1.04x slower                                                |
| unpickle                 | 14.4 us                                                | 15.1 us: 1.05x slower                                                |
| pickle                   | 10.7 us                                                | 12.0 us: 1.13x slower                                                |
| telco                    | 7.27 ms                                                | 8.50 ms: 1.17x slower                                                |
| float                    | 117 ms                                                 | 139 ms: 1.19x slower                                                 |
| pickle_dict              | 29.6 us                                                | 36.3 us: 1.23x slower                                                |
| coverage                 | 79.4 ms                                                | 99.1 ms: 1.25x slower                                                |
| async_generators         | 444 ms                                                 | 557 ms: 1.26x slower                                                 |
| xml_etree_parse          | 168 ms                                                 | 219 ms: 1.30x slower                                                 |
| xml_etree_iterparse      | 115 ms                                                 | 162 ms: 1.40x slower                                                 |
| docutils                 | 3.30 sec                                               | 4.82 sec: 1.46x slower                                               |
| python_startup_no_site   | 5.93 ms                                                | 10.1 ms: 1.70x slower                                                |
| dask                     | 441 ms                                                 | 766 ms: 1.74x slower                                                 |
| pylint                   | 551 ms                                                 | 1.01 sec: 1.84x slower                                               |
| unpack_sequence          | 60.0 ns                                                | 113 ns: 1.88x slower                                                 |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 4.17 sec: 4.11x slower                                               |
| async_tree_none          | 728 ms                                                 | 3.43 sec: 4.71x slower                                               |
| async_tree_memoization   | 870 ms                                                 | 4.43 sec: 5.09x slower                                               |
| async_tree_io            | 1.77 sec                                               | 13.3 sec: 7.50x slower                                               |
| Geometric mean           | (ref)                                                  | 1.14x faster                                                         |

Benchmark hidden because not significant (4): unpickle_list, xml_etree_generate, regex_dna, bench_mp_pool
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240321-3.13.0a5+-98575b4-JIT/bm-20240321-linux-x86_64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.15x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.08x


# Memory

- memory change: 1.21x