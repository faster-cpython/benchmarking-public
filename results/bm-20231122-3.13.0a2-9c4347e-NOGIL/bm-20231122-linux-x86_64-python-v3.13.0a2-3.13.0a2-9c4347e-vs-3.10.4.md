# Results vs. 3.10.4

- fork: python
- ref: v3.13.0a2
- machine: linux-x86_64
- commit hash: 9c4347e
- commit date: 2023-11-22
- overall geometric mean: 1.09x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x faster
- Memory change: 0.65x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 294 ms: 1.19x faster                                       |
| chameleon      | 9.68 ms                                                | 7.76 ms: 1.25x faster                                      |
| docutils       | 3.30 sec                                               | 2.89 sec: 1.14x faster                                     |
| html5lib       | 88.9 ms                                                | 71.7 ms: 1.24x faster                                      |
| tornado_http   | 136 ms                                                 | 108 ms: 1.27x faster                                       |
| Geometric mean | (ref)                                                  | 1.22x faster                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 509 ms: 1.43x faster                                       |
| async_tree_memoization  | 870 ms                                                 | 657 ms: 1.32x faster                                       |
| async_tree_io           | 1.77 sec                                               | 1.39 sec: 1.27x faster                                     |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 804 ms: 1.26x faster                                       |
| Geometric mean          | (ref)                                                  | 1.32x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 154 ms                                                 | 110 ms: 1.40x faster                                       |
| float          | 117 ms                                                 | 95.5 ms: 1.23x faster                                      |
| pidigits       | 191 ms                                                 | 194 ms: 1.01x slower                                       |
| Geometric mean | (ref)                                                  | 1.19x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 149 ms: 1.26x faster                                       |
| regex_v8       | 27.8 ms                                                | 25.9 ms: 1.07x faster                                      |
| regex_dna      | 227 ms                                                 | 222 ms: 1.02x faster                                       |
| regex_effbot   | 3.63 ms                                                | 3.83 ms: 1.05x slower                                      |
| Geometric mean | (ref)                                                  | 1.07x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 335 us: 1.45x faster                                       |
| unpickle_pure_python | 331 us                                                 | 246 us: 1.35x faster                                       |
| tomli_loads          | 3.14 sec                                               | 2.37 sec: 1.33x faster                                     |
| json_dumps           | 14.2 ms                                                | 11.3 ms: 1.26x faster                                      |
| pickle_list          | 5.08 us                                                | 4.71 us: 1.08x faster                                      |
| xml_etree_iterparse  | 115 ms                                                 | 114 ms: 1.01x faster                                       |
| json_loads           | 31.2 us                                                | 30.9 us: 1.01x faster                                      |
| unpickle_list        | 5.20 us                                                | 5.26 us: 1.01x slower                                      |
| pickle               | 10.7 us                                                | 11.4 us: 1.07x slower                                      |
| unpickle             | 14.4 us                                                | 15.4 us: 1.07x slower                                      |
| pickle_dict          | 29.6 us                                                | 32.7 us: 1.11x slower                                      |
| xml_etree_parse      | 168 ms                                                 | 472 ms: 2.81x slower                                       |
| xml_etree_process    | 79.1 ms                                                | 1.03 sec: 13.00x slower                                    |
| xml_etree_generate   | 99.4 ms                                                | 1.58 sec: 15.91x slower                                    |
| Geometric mean       | (ref)                                                  | 1.46x slower                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 11.1 ms: 1.31x faster                                      |
| python_startup_no_site | 5.93 ms                                                | 9.60 ms: 1.62x slower                                      |
| Geometric mean         | (ref)                                                  | 1.11x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 24.9 ms: 1.28x faster                                      |
| mako            | 16.3 ms                                                | 12.9 ms: 1.26x faster                                      |
| django_template | 48.2 ms                                                | 38.3 ms: 1.26x faster                                      |
| genshi_xml      | 66.0 ms                                                | 56.2 ms: 1.18x faster                                      |
| Geometric mean  | (ref)                                                  | 1.24x faster                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 127 us: 4.28x faster                                       |
| generators               | 80.1 ms                                                | 31.2 ms: 2.56x faster                                      |
| deltablue                | 7.91 ms                                                | 3.99 ms: 1.98x faster                                      |
| asyncio_tcp              | 922 ms                                                 | 511 ms: 1.80x faster                                       |
| chaos                    | 115 ms                                                 | 68.7 ms: 1.68x faster                                      |
| logging_silent           | 190 ns                                                 | 116 ns: 1.64x faster                                       |
| pylint                   | 551 ms                                                 | 341 ms: 1.62x faster                                       |
| raytrace                 | 507 ms                                                 | 314 ms: 1.62x faster                                       |
| richards_super           | 94.7 ms                                                | 59.1 ms: 1.60x faster                                      |
| crypto_pyaes             | 128 ms                                                 | 80.1 ms: 1.59x faster                                      |
| scimark_sor              | 220 ms                                                 | 140 ms: 1.57x faster                                       |
| comprehensions           | 28.8 us                                                | 18.5 us: 1.56x faster                                      |
| scimark_monte_carlo      | 118 ms                                                 | 76.1 ms: 1.55x faster                                      |
| go                       | 240 ms                                                 | 157 ms: 1.53x faster                                       |
| richards                 | 79.3 ms                                                | 51.9 ms: 1.53x faster                                      |
| hexiom                   | 10.4 ms                                                | 6.86 ms: 1.51x faster                                      |
| sqlglot_parse            | 2.17 ms                                                | 1.44 ms: 1.51x faster                                      |
| pickle_pure_python       | 484 us                                                 | 335 us: 1.45x faster                                       |
| sqlglot_transpile        | 2.57 ms                                                | 1.79 ms: 1.44x faster                                      |
| async_tree_none          | 728 ms                                                 | 509 ms: 1.43x faster                                       |
| coroutines               | 35.1 ms                                                | 24.8 ms: 1.42x faster                                      |
| pyflate                  | 716 ms                                                 | 510 ms: 1.41x faster                                       |
| nbody                    | 154 ms                                                 | 110 ms: 1.40x faster                                       |
| scimark_lu               | 176 ms                                                 | 126 ms: 1.39x faster                                       |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.85 sec: 1.39x faster                                     |
| deepcopy_memo            | 58.5 us                                                | 43.0 us: 1.36x faster                                      |
| unpickle_pure_python     | 331 us                                                 | 246 us: 1.35x faster                                       |
| create_gc_cycles         | 1.62 ms                                                | 1.22 ms: 1.33x faster                                      |
| tomli_loads              | 3.14 sec                                               | 2.37 sec: 1.33x faster                                     |
| async_tree_memoization   | 870 ms                                                 | 657 ms: 1.32x faster                                       |
| python_startup           | 14.6 ms                                                | 11.1 ms: 1.31x faster                                      |
| spectral_norm            | 170 ms                                                 | 130 ms: 1.31x faster                                       |
| logging_simple           | 8.30 us                                                | 6.44 us: 1.29x faster                                      |
| logging_format           | 9.09 us                                                | 7.09 us: 1.28x faster                                      |
| genshi_text              | 31.8 ms                                                | 24.9 ms: 1.28x faster                                      |
| async_tree_io            | 1.77 sec                                               | 1.39 sec: 1.27x faster                                     |
| tornado_http             | 136 ms                                                 | 108 ms: 1.27x faster                                       |
| pprint_pformat           | 2.10 sec                                               | 1.66 sec: 1.27x faster                                     |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 804 ms: 1.26x faster                                       |
| mako                     | 16.3 ms                                                | 12.9 ms: 1.26x faster                                      |
| regex_compile            | 188 ms                                                 | 149 ms: 1.26x faster                                       |
| json_dumps               | 14.2 ms                                                | 11.3 ms: 1.26x faster                                      |
| django_template          | 48.2 ms                                                | 38.3 ms: 1.26x faster                                      |
| pprint_safe_repr         | 1.02 sec                                               | 812 ms: 1.25x faster                                       |
| chameleon                | 9.68 ms                                                | 7.76 ms: 1.25x faster                                      |
| html5lib                 | 88.9 ms                                                | 71.7 ms: 1.24x faster                                      |
| pycparser                | 1.58 sec                                               | 1.27 sec: 1.24x faster                                     |
| float                    | 117 ms                                                 | 95.5 ms: 1.23x faster                                      |
| deepcopy                 | 479 us                                                 | 392 us: 1.22x faster                                       |
| sqlglot_normalize        | 143 ms                                                 | 118 ms: 1.21x faster                                       |
| nqueens                  | 106 ms                                                 | 88.6 ms: 1.19x faster                                      |
| dulwich_log              | 84.3 ms                                                | 70.8 ms: 1.19x faster                                      |
| 2to3                     | 348 ms                                                 | 294 ms: 1.19x faster                                       |
| deepcopy_reduce          | 4.17 us                                                | 3.53 us: 1.18x faster                                      |
| fannkuch                 | 532 ms                                                 | 451 ms: 1.18x faster                                       |
| genshi_xml               | 66.0 ms                                                | 56.2 ms: 1.18x faster                                      |
| sqlglot_optimize         | 69.2 ms                                                | 59.4 ms: 1.16x faster                                      |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.61 ms: 1.15x faster                                      |
| aiohttp                  | 1.44 ms                                                | 1.25 ms: 1.15x faster                                      |
| scimark_fft              | 466 ms                                                 | 405 ms: 1.15x faster                                       |
| docutils                 | 3.30 sec                                               | 2.89 sec: 1.14x faster                                     |
| gunicorn                 | 1.53 ms                                                | 1.35 ms: 1.14x faster                                      |
| sympy_integrate          | 25.8 ms                                                | 22.9 ms: 1.13x faster                                      |
| pickle_list              | 5.08 us                                                | 4.71 us: 1.08x faster                                      |
| regex_v8                 | 27.8 ms                                                | 25.9 ms: 1.07x faster                                      |
| bench_mp_pool            | 24.0 ms                                                | 22.6 ms: 1.06x faster                                      |
| sympy_str                | 346 ms                                                 | 332 ms: 1.04x faster                                       |
| pathlib                  | 20.5 ms                                                | 19.8 ms: 1.03x faster                                      |
| meteor_contest           | 120 ms                                                 | 117 ms: 1.02x faster                                       |
| regex_dna                | 227 ms                                                 | 222 ms: 1.02x faster                                       |
| xml_etree_iterparse      | 115 ms                                                 | 114 ms: 1.01x faster                                       |
| json_loads               | 31.2 us                                                | 30.9 us: 1.01x faster                                      |
| gc_traversal             | 3.62 ms                                                | 3.64 ms: 1.01x slower                                      |
| asyncio_websockets       | 559 ms                                                 | 564 ms: 1.01x slower                                       |
| unpickle_list            | 5.20 us                                                | 5.26 us: 1.01x slower                                      |
| pidigits                 | 191 ms                                                 | 194 ms: 1.01x slower                                       |
| mdp                      | 2.85 sec                                               | 2.89 sec: 1.02x slower                                     |
| regex_effbot             | 3.63 ms                                                | 3.83 ms: 1.05x slower                                      |
| sqlite_synth             | 3.02 us                                                | 3.23 us: 1.07x slower                                      |
| pickle                   | 10.7 us                                                | 11.4 us: 1.07x slower                                      |
| unpickle                 | 14.4 us                                                | 15.4 us: 1.07x slower                                      |
| sympy_sum                | 196 ms                                                 | 211 ms: 1.07x slower                                       |
| sympy_expand             | 566 ms                                                 | 613 ms: 1.08x slower                                       |
| bench_thread_pool        | 986 us                                                 | 1.09 ms: 1.10x slower                                      |
| pickle_dict              | 29.6 us                                                | 32.7 us: 1.11x slower                                      |
| async_generators         | 444 ms                                                 | 500 ms: 1.13x slower                                       |
| flaskblogging            | 8.58 ms                                                | 10.2 ms: 1.19x slower                                      |
| mypy2                    | 894 ms                                                 | 1.15 sec: 1.29x slower                                     |
| telco                    | 7.27 ms                                                | 9.60 ms: 1.32x slower                                      |
| python_startup_no_site   | 5.93 ms                                                | 9.60 ms: 1.62x slower                                      |
| xml_etree_parse          | 168 ms                                                 | 472 ms: 2.81x slower                                       |
| thrift                   | 1.07 ms                                                | 9.50 ms: 8.87x slower                                      |
| coverage                 | 79.4 ms                                                | 725 ms: 9.13x slower                                       |
| xml_etree_process        | 79.1 ms                                                | 1.03 sec: 13.00x slower                                    |
| xml_etree_generate       | 99.4 ms                                                | 1.58 sec: 15.91x slower                                    |
| Geometric mean           | (ref)                                                  | 1.09x faster                                               |

Benchmark hidden because not significant (1): json
Ignored benchmarks (5) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: dask, djangocms, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20231122-3.13.0a2-9c4347e-NOGIL/bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.14x

# Memory
- memory change: 0.65x