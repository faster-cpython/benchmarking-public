# Results vs. 3.10.4

- fork: brandtbucher
- ref: dynamic_exit
- machine: linux-x86_64
- commit hash: a8158ae
- commit date: 2024-05-05
- overall geometric mean: 1.08x faster
- HPT reliability: 99.52%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240505-linux-x86_64-brandtbucher-dynamic_exit-3.13.0a6+-a8158ae |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 357 ms: 1.03x slower                                                 |
| chameleon      | 9.68 ms                                                | 9.02 ms: 1.07x faster                                                |
| html5lib       | 88.9 ms                                                | 83.5 ms: 1.06x faster                                                |
| tornado_http   | 136 ms                                                 | 108 ms: 1.26x faster                                                 |
| Geometric mean | (ref)                                                  | 1.09x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240505-linux-x86_64-brandtbucher-dynamic_exit-3.13.0a6+-a8158ae |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 411 ms: 1.77x faster                                                 |
| async_tree_io           | 1.77 sec                                               | 1.05 sec: 1.68x faster                                               |
| async_tree_memoization  | 870 ms                                                 | 532 ms: 1.63x faster                                                 |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 666 ms: 1.52x faster                                                 |
| Geometric mean          | (ref)                                                  | 1.65x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240505-linux-x86_64-brandtbucher-dynamic_exit-3.13.0a6+-a8158ae |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 117 ms                                                 | 92.6 ms: 1.26x faster                                                |
| nbody          | 154 ms                                                 | 123 ms: 1.25x faster                                                 |
| pidigits       | 191 ms                                                 | 193 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                  | 1.16x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240505-linux-x86_64-brandtbucher-dynamic_exit-3.13.0a6+-a8158ae |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_v8       | 27.8 ms                                                | 27.1 ms: 1.03x faster                                                |
| regex_dna      | 227 ms                                                 | 223 ms: 1.02x faster                                                 |
| regex_effbot   | 3.63 ms                                                | 3.75 ms: 1.03x slower                                                |
| regex_compile  | 188 ms                                                 | 220 ms: 1.17x slower                                                 |
| Geometric mean | (ref)                                                  | 1.04x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240505-linux-x86_64-brandtbucher-dynamic_exit-3.13.0a6+-a8158ae |
|---------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| json_dumps          | 14.2 ms                                                | 11.5 ms: 1.23x faster                                                |
| json_loads          | 31.2 us                                                | 27.7 us: 1.13x faster                                                |
| tomli_loads         | 3.14 sec                                               | 2.81 sec: 1.12x faster                                               |
| xml_etree_process   | 79.1 ms                                                | 71.4 ms: 1.11x faster                                                |
| xml_etree_parse     | 168 ms                                                 | 154 ms: 1.09x faster                                                 |
| xml_etree_iterparse | 115 ms                                                 | 111 ms: 1.04x faster                                                 |
| pickle_list         | 5.08 us                                                | 5.03 us: 1.01x faster                                                |
| xml_etree_generate  | 99.4 ms                                                | 104 ms: 1.04x slower                                                 |
| pickle_pure_python  | 484 us                                                 | 525 us: 1.08x slower                                                 |
| unpickle            | 14.4 us                                                | 15.7 us: 1.09x slower                                                |
| pickle              | 10.7 us                                                | 12.1 us: 1.14x slower                                                |
| pickle_dict         | 29.6 us                                                | 36.0 us: 1.22x slower                                                |
| Geometric mean      | (ref)                                                  | 1.01x faster                                                         |

Benchmark hidden because not significant (2): unpickle_list, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240505-linux-x86_64-brandtbucher-dynamic_exit-3.13.0a6+-a8158ae |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.8 ms: 1.35x faster                                                |
| python_startup_no_site | 5.93 ms                                                | 7.25 ms: 1.22x slower                                                |
| Geometric mean         | (ref)                                                  | 1.05x faster                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240505-linux-x86_64-brandtbucher-dynamic_exit-3.13.0a6+-a8158ae |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 14.2 ms: 1.15x faster                                                |
| django_template | 48.2 ms                                                | 49.2 ms: 1.02x slower                                                |
| genshi_text     | 31.8 ms                                                | 39.8 ms: 1.25x slower                                                |
| genshi_xml      | 66.0 ms                                                | 82.8 ms: 1.25x slower                                                |
| Geometric mean  | (ref)                                                  | 1.09x slower                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240505-linux-x86_64-brandtbucher-dynamic_exit-3.13.0a6+-a8158ae |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 217 us: 2.51x faster                                                 |
| async_tree_none          | 728 ms                                                 | 411 ms: 1.77x faster                                                 |
| asyncio_tcp              | 922 ms                                                 | 526 ms: 1.75x faster                                                 |
| deltablue                | 7.91 ms                                                | 4.67 ms: 1.69x faster                                                |
| async_tree_io            | 1.77 sec                                               | 1.05 sec: 1.68x faster                                               |
| async_tree_memoization   | 870 ms                                                 | 532 ms: 1.63x faster                                                 |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 666 ms: 1.52x faster                                                 |
| raytrace                 | 507 ms                                                 | 357 ms: 1.42x faster                                                 |
| coroutines               | 35.1 ms                                                | 24.8 ms: 1.42x faster                                                |
| pylint                   | 551 ms                                                 | 396 ms: 1.39x faster                                                 |
| scimark_sor              | 220 ms                                                 | 158 ms: 1.39x faster                                                 |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.87 sec: 1.37x faster                                               |
| python_startup           | 14.6 ms                                                | 10.8 ms: 1.35x faster                                                |
| chaos                    | 115 ms                                                 | 87.6 ms: 1.32x faster                                                |
| thrift                   | 1.07 ms                                                | 832 us: 1.29x faster                                                 |
| crypto_pyaes             | 128 ms                                                 | 99.9 ms: 1.28x faster                                                |
| float                    | 117 ms                                                 | 92.6 ms: 1.26x faster                                                |
| tornado_http             | 136 ms                                                 | 108 ms: 1.26x faster                                                 |
| logging_silent           | 190 ns                                                 | 152 ns: 1.25x faster                                                 |
| nbody                    | 154 ms                                                 | 123 ms: 1.25x faster                                                 |
| spectral_norm            | 170 ms                                                 | 137 ms: 1.24x faster                                                 |
| json_dumps               | 14.2 ms                                                | 11.5 ms: 1.23x faster                                                |
| generators               | 80.1 ms                                                | 65.9 ms: 1.21x faster                                                |
| sqlglot_parse            | 2.17 ms                                                | 1.81 ms: 1.20x faster                                                |
| richards_super           | 94.7 ms                                                | 79.4 ms: 1.19x faster                                                |
| logging_simple           | 8.30 us                                                | 6.97 us: 1.19x faster                                                |
| scimark_monte_carlo      | 118 ms                                                 | 99.5 ms: 1.19x faster                                                |
| logging_format           | 9.09 us                                                | 7.83 us: 1.16x faster                                                |
| pyflate                  | 716 ms                                                 | 619 ms: 1.16x faster                                                 |
| go                       | 240 ms                                                 | 208 ms: 1.16x faster                                                 |
| mako                     | 16.3 ms                                                | 14.2 ms: 1.15x faster                                                |
| sqlglot_transpile        | 2.57 ms                                                | 2.24 ms: 1.15x faster                                                |
| djangocms                | 38.4 us                                                | 33.5 us: 1.15x faster                                                |
| json_loads               | 31.2 us                                                | 27.7 us: 1.13x faster                                                |
| tomli_loads              | 3.14 sec                                               | 2.81 sec: 1.12x faster                                               |
| richards                 | 79.3 ms                                                | 71.0 ms: 1.12x faster                                                |
| dask                     | 441 ms                                                 | 395 ms: 1.12x faster                                                 |
| xml_etree_process        | 79.1 ms                                                | 71.4 ms: 1.11x faster                                                |
| aiohttp                  | 1.44 ms                                                | 1.30 ms: 1.10x faster                                                |
| fannkuch                 | 532 ms                                                 | 483 ms: 1.10x faster                                                 |
| xml_etree_parse          | 168 ms                                                 | 154 ms: 1.09x faster                                                 |
| gunicorn                 | 1.53 ms                                                | 1.41 ms: 1.09x faster                                                |
| dulwich_log              | 84.3 ms                                                | 77.9 ms: 1.08x faster                                                |
| pathlib                  | 20.5 ms                                                | 19.0 ms: 1.08x faster                                                |
| chameleon                | 9.68 ms                                                | 9.02 ms: 1.07x faster                                                |
| html5lib                 | 88.9 ms                                                | 83.5 ms: 1.06x faster                                                |
| comprehensions           | 28.8 us                                                | 27.1 us: 1.06x faster                                                |
| scimark_fft              | 466 ms                                                 | 445 ms: 1.05x faster                                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 6.20 ms: 1.04x faster                                                |
| xml_etree_iterparse      | 115 ms                                                 | 111 ms: 1.04x faster                                                 |
| deepcopy_memo            | 58.5 us                                                | 56.6 us: 1.03x faster                                                |
| json                     | 5.69 ms                                                | 5.53 ms: 1.03x faster                                                |
| scimark_lu               | 176 ms                                                 | 171 ms: 1.03x faster                                                 |
| regex_v8                 | 27.8 ms                                                | 27.1 ms: 1.03x faster                                                |
| regex_dna                | 227 ms                                                 | 223 ms: 1.02x faster                                                 |
| sympy_sum                | 196 ms                                                 | 194 ms: 1.01x faster                                                 |
| pickle_list              | 5.08 us                                                | 5.03 us: 1.01x faster                                                |
| bench_thread_pool        | 986 us                                                 | 991 us: 1.01x slower                                                 |
| sympy_integrate          | 25.8 ms                                                | 25.9 ms: 1.01x slower                                                |
| pidigits                 | 191 ms                                                 | 193 ms: 1.01x slower                                                 |
| asyncio_websockets       | 559 ms                                                 | 567 ms: 1.01x slower                                                 |
| pycparser                | 1.58 sec                                               | 1.60 sec: 1.02x slower                                               |
| mdp                      | 2.85 sec                                               | 2.91 sec: 1.02x slower                                               |
| django_template          | 48.2 ms                                                | 49.2 ms: 1.02x slower                                                |
| sqlite_synth             | 3.02 us                                                | 3.10 us: 1.02x slower                                                |
| 2to3                     | 348 ms                                                 | 357 ms: 1.03x slower                                                 |
| hexiom                   | 10.4 ms                                                | 10.7 ms: 1.03x slower                                                |
| regex_effbot             | 3.63 ms                                                | 3.75 ms: 1.03x slower                                                |
| xml_etree_generate       | 99.4 ms                                                | 104 ms: 1.04x slower                                                 |
| sympy_str                | 346 ms                                                 | 366 ms: 1.06x slower                                                 |
| deepcopy_reduce          | 4.17 us                                                | 4.45 us: 1.07x slower                                                |
| gc_traversal             | 3.62 ms                                                | 3.88 ms: 1.07x slower                                                |
| sqlglot_normalize        | 143 ms                                                 | 154 ms: 1.08x slower                                                 |
| meteor_contest           | 120 ms                                                 | 129 ms: 1.08x slower                                                 |
| deepcopy                 | 479 us                                                 | 518 us: 1.08x slower                                                 |
| pickle_pure_python       | 484 us                                                 | 525 us: 1.08x slower                                                 |
| sympy_expand             | 566 ms                                                 | 614 ms: 1.09x slower                                                 |
| sqlglot_optimize         | 69.2 ms                                                | 75.4 ms: 1.09x slower                                                |
| unpickle                 | 14.4 us                                                | 15.7 us: 1.09x slower                                                |
| flaskblogging            | 8.58 ms                                                | 9.59 ms: 1.12x slower                                                |
| async_generators         | 444 ms                                                 | 504 ms: 1.14x slower                                                 |
| pickle                   | 10.7 us                                                | 12.1 us: 1.14x slower                                                |
| create_gc_cycles         | 1.62 ms                                                | 1.87 ms: 1.16x slower                                                |
| coverage                 | 79.4 ms                                                | 92.4 ms: 1.16x slower                                                |
| regex_compile            | 188 ms                                                 | 220 ms: 1.17x slower                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 1.21 sec: 1.19x slower                                               |
| pprint_pformat           | 2.10 sec                                               | 2.55 sec: 1.21x slower                                               |
| pickle_dict              | 29.6 us                                                | 36.0 us: 1.22x slower                                                |
| python_startup_no_site   | 5.93 ms                                                | 7.25 ms: 1.22x slower                                                |
| genshi_text              | 31.8 ms                                                | 39.8 ms: 1.25x slower                                                |
| genshi_xml               | 66.0 ms                                                | 82.8 ms: 1.25x slower                                                |
| nqueens                  | 106 ms                                                 | 141 ms: 1.33x slower                                                 |
| telco                    | 7.27 ms                                                | 10.7 ms: 1.47x slower                                                |
| Geometric mean           | (ref)                                                  | 1.08x faster                                                         |

Benchmark hidden because not significant (4): mypy2, unpickle_list, bench_mp_pool, unpickle_pure_python
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: docutils, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240505-3.13.0a6+-a8158ae-PYTHON_UOPS/bm-20240505-linux-x86_64-brandtbucher-dynamic_exit-3.13.0a6+-a8158ae.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 99.52% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.12x