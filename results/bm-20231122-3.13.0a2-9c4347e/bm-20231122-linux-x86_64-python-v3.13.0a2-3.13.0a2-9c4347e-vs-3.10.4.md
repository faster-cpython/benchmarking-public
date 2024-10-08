# Results vs. 3.10.4

- fork: python
- ref: v3.13.0a2
- machine: linux-x86_64
- commit hash: 9c4347e
- commit date: 2023-11-22
- overall geometric mean: 1.32x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 272 ms: 1.28x faster                                       |
| chameleon      | 9.68 ms                                                | 6.93 ms: 1.40x faster                                      |
| docutils       | 3.30 sec                                               | 2.69 sec: 1.23x faster                                     |
| html5lib       | 88.9 ms                                                | 66.3 ms: 1.34x faster                                      |
| tornado_http   | 136 ms                                                 | 97.6 ms: 1.40x faster                                      |
| Geometric mean | (ref)                                                  | 1.33x faster                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 451 ms: 1.62x faster                                       |
| async_tree_memoization  | 870 ms                                                 | 583 ms: 1.49x faster                                       |
| async_tree_io           | 1.77 sec                                               | 1.22 sec: 1.44x faster                                     |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 733 ms: 1.39x faster                                       |
| Geometric mean          | (ref)                                                  | 1.48x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 154 ms                                                 | 91.0 ms: 1.69x faster                                      |
| float          | 117 ms                                                 | 83.5 ms: 1.40x faster                                      |
| pidigits       | 191 ms                                                 | 197 ms: 1.03x slower                                       |
| Geometric mean | (ref)                                                  | 1.32x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 137 ms: 1.37x faster                                       |
| regex_v8       | 27.8 ms                                                | 25.0 ms: 1.11x faster                                      |
| regex_dna      | 227 ms                                                 | 219 ms: 1.03x faster                                       |
| regex_effbot   | 3.63 ms                                                | 3.57 ms: 1.02x faster                                      |
| Geometric mean | (ref)                                                  | 1.13x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 313 us: 1.55x faster                                       |
| unpickle_pure_python | 331 us                                                 | 224 us: 1.48x faster                                       |
| tomli_loads          | 3.14 sec                                               | 2.23 sec: 1.41x faster                                     |
| json_dumps           | 14.2 ms                                                | 10.7 ms: 1.33x faster                                      |
| xml_etree_process    | 79.1 ms                                                | 60.5 ms: 1.31x faster                                      |
| xml_etree_generate   | 99.4 ms                                                | 88.2 ms: 1.13x faster                                      |
| json_loads           | 31.2 us                                                | 28.7 us: 1.09x faster                                      |
| xml_etree_iterparse  | 115 ms                                                 | 108 ms: 1.07x faster                                       |
| xml_etree_parse      | 168 ms                                                 | 162 ms: 1.04x faster                                       |
| unpickle_list        | 5.20 us                                                | 5.12 us: 1.02x faster                                      |
| unpickle             | 14.4 us                                                | 15.7 us: 1.09x slower                                      |
| pickle               | 10.7 us                                                | 11.8 us: 1.11x slower                                      |
| pickle_dict          | 29.6 us                                                | 34.9 us: 1.18x slower                                      |
| Geometric mean       | (ref)                                                  | 1.13x faster                                               |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.7 ms: 1.37x faster                                      |
| python_startup_no_site | 5.93 ms                                                | 9.26 ms: 1.56x slower                                      |
| Geometric mean         | (ref)                                                  | 1.07x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.7 ms: 1.40x faster                                      |
| django_template | 48.2 ms                                                | 35.2 ms: 1.37x faster                                      |
| genshi_text     | 31.8 ms                                                | 23.8 ms: 1.34x faster                                      |
| genshi_xml      | 66.0 ms                                                | 52.1 ms: 1.27x faster                                      |
| Geometric mean  | (ref)                                                  | 1.34x faster                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 119 us: 4.57x faster                                       |
| generators               | 80.1 ms                                                | 30.1 ms: 2.66x faster                                      |
| deltablue                | 7.91 ms                                                | 3.44 ms: 2.30x faster                                      |
| asyncio_tcp              | 922 ms                                                 | 501 ms: 1.84x faster                                       |
| chaos                    | 115 ms                                                 | 63.4 ms: 1.82x faster                                      |
| raytrace                 | 507 ms                                                 | 284 ms: 1.78x faster                                       |
| pylint                   | 551 ms                                                 | 313 ms: 1.76x faster                                       |
| logging_silent           | 190 ns                                                 | 109 ns: 1.74x faster                                       |
| crypto_pyaes             | 128 ms                                                 | 73.3 ms: 1.74x faster                                      |
| scimark_sor              | 220 ms                                                 | 126 ms: 1.74x faster                                       |
| richards_super           | 94.7 ms                                                | 55.1 ms: 1.72x faster                                      |
| scimark_monte_carlo      | 118 ms                                                 | 70.0 ms: 1.69x faster                                      |
| nbody                    | 154 ms                                                 | 91.0 ms: 1.69x faster                                      |
| comprehensions           | 28.8 us                                                | 17.0 us: 1.69x faster                                      |
| sqlglot_parse            | 2.17 ms                                                | 1.31 ms: 1.65x faster                                      |
| hexiom                   | 10.4 ms                                                | 6.32 ms: 1.65x faster                                      |
| go                       | 240 ms                                                 | 148 ms: 1.63x faster                                       |
| async_tree_none          | 728 ms                                                 | 451 ms: 1.62x faster                                       |
| coroutines               | 35.1 ms                                                | 21.8 ms: 1.61x faster                                      |
| richards                 | 79.3 ms                                                | 49.7 ms: 1.60x faster                                      |
| sqlglot_transpile        | 2.57 ms                                                | 1.64 ms: 1.57x faster                                      |
| pickle_pure_python       | 484 us                                                 | 313 us: 1.55x faster                                       |
| spectral_norm            | 170 ms                                                 | 111 ms: 1.53x faster                                       |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.51x faster                                       |
| async_tree_memoization   | 870 ms                                                 | 583 ms: 1.49x faster                                       |
| pyflate                  | 716 ms                                                 | 484 ms: 1.48x faster                                       |
| unpickle_pure_python     | 331 us                                                 | 224 us: 1.48x faster                                       |
| deepcopy_memo            | 58.5 us                                                | 39.8 us: 1.47x faster                                      |
| async_tree_io            | 1.77 sec                                               | 1.22 sec: 1.44x faster                                     |
| tomli_loads              | 3.14 sec                                               | 2.23 sec: 1.41x faster                                     |
| logging_simple           | 8.30 us                                                | 5.89 us: 1.41x faster                                      |
| float                    | 117 ms                                                 | 83.5 ms: 1.40x faster                                      |
| mako                     | 16.3 ms                                                | 11.7 ms: 1.40x faster                                      |
| logging_format           | 9.09 us                                                | 6.50 us: 1.40x faster                                      |
| chameleon                | 9.68 ms                                                | 6.93 ms: 1.40x faster                                      |
| tornado_http             | 136 ms                                                 | 97.6 ms: 1.40x faster                                      |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.84 sec: 1.40x faster                                     |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 733 ms: 1.39x faster                                       |
| regex_compile            | 188 ms                                                 | 137 ms: 1.37x faster                                       |
| pprint_pformat           | 2.10 sec                                               | 1.54 sec: 1.37x faster                                     |
| python_startup           | 14.6 ms                                                | 10.7 ms: 1.37x faster                                      |
| django_template          | 48.2 ms                                                | 35.2 ms: 1.37x faster                                      |
| deepcopy                 | 479 us                                                 | 354 us: 1.36x faster                                       |
| pprint_safe_repr         | 1.02 sec                                               | 753 ms: 1.35x faster                                       |
| html5lib                 | 88.9 ms                                                | 66.3 ms: 1.34x faster                                      |
| genshi_text              | 31.8 ms                                                | 23.8 ms: 1.34x faster                                      |
| sqlglot_normalize        | 143 ms                                                 | 107 ms: 1.33x faster                                       |
| thrift                   | 1.07 ms                                                | 805 us: 1.33x faster                                       |
| json_dumps               | 14.2 ms                                                | 10.7 ms: 1.33x faster                                      |
| deepcopy_reduce          | 4.17 us                                                | 3.14 us: 1.33x faster                                      |
| pycparser                | 1.58 sec                                               | 1.19 sec: 1.32x faster                                     |
| fannkuch                 | 532 ms                                                 | 402 ms: 1.32x faster                                       |
| xml_etree_process        | 79.1 ms                                                | 60.5 ms: 1.31x faster                                      |
| sympy_sum                | 196 ms                                                 | 151 ms: 1.30x faster                                       |
| sympy_integrate          | 25.8 ms                                                | 20.0 ms: 1.29x faster                                      |
| 2to3                     | 348 ms                                                 | 272 ms: 1.28x faster                                       |
| sqlglot_optimize         | 69.2 ms                                                | 54.3 ms: 1.27x faster                                      |
| sympy_str                | 346 ms                                                 | 273 ms: 1.27x faster                                       |
| genshi_xml               | 66.0 ms                                                | 52.1 ms: 1.27x faster                                      |
| nqueens                  | 106 ms                                                 | 83.5 ms: 1.27x faster                                      |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.13 ms: 1.26x faster                                      |
| dulwich_log              | 84.3 ms                                                | 67.6 ms: 1.25x faster                                      |
| scimark_fft              | 466 ms                                                 | 375 ms: 1.24x faster                                       |
| sympy_expand             | 566 ms                                                 | 459 ms: 1.23x faster                                       |
| aiohttp                  | 1.44 ms                                                | 1.17 ms: 1.23x faster                                      |
| docutils                 | 3.30 sec                                               | 2.69 sec: 1.23x faster                                     |
| djangocms                | 38.4 us                                                | 31.4 us: 1.23x faster                                      |
| gunicorn                 | 1.53 ms                                                | 1.27 ms: 1.21x faster                                      |
| bench_thread_pool        | 986 us                                                 | 852 us: 1.16x faster                                       |
| xml_etree_generate       | 99.4 ms                                                | 88.2 ms: 1.13x faster                                      |
| regex_v8                 | 27.8 ms                                                | 25.0 ms: 1.11x faster                                      |
| pathlib                  | 20.5 ms                                                | 18.6 ms: 1.10x faster                                      |
| create_gc_cycles         | 1.62 ms                                                | 1.48 ms: 1.09x faster                                      |
| json_loads               | 31.2 us                                                | 28.7 us: 1.09x faster                                      |
| json                     | 5.69 ms                                                | 5.24 ms: 1.09x faster                                      |
| meteor_contest           | 120 ms                                                 | 110 ms: 1.08x faster                                       |
| mdp                      | 2.85 sec                                               | 2.64 sec: 1.08x faster                                     |
| xml_etree_iterparse      | 115 ms                                                 | 108 ms: 1.07x faster                                       |
| sqlite_synth             | 3.02 us                                                | 2.87 us: 1.05x faster                                      |
| xml_etree_parse          | 168 ms                                                 | 162 ms: 1.04x faster                                       |
| regex_dna                | 227 ms                                                 | 219 ms: 1.03x faster                                       |
| regex_effbot             | 3.63 ms                                                | 3.57 ms: 1.02x faster                                      |
| unpickle_list            | 5.20 us                                                | 5.12 us: 1.02x faster                                      |
| asyncio_websockets       | 559 ms                                                 | 563 ms: 1.01x slower                                       |
| flaskblogging            | 8.58 ms                                                | 8.70 ms: 1.01x slower                                      |
| async_generators         | 444 ms                                                 | 459 ms: 1.03x slower                                       |
| pidigits                 | 191 ms                                                 | 197 ms: 1.03x slower                                       |
| unpickle                 | 14.4 us                                                | 15.7 us: 1.09x slower                                      |
| pickle                   | 10.7 us                                                | 11.8 us: 1.11x slower                                      |
| telco                    | 7.27 ms                                                | 8.53 ms: 1.17x slower                                      |
| pickle_dict              | 29.6 us                                                | 34.9 us: 1.18x slower                                      |
| coverage                 | 79.4 ms                                                | 95.2 ms: 1.20x slower                                      |
| gc_traversal             | 3.62 ms                                                | 4.37 ms: 1.21x slower                                      |
| python_startup_no_site   | 5.93 ms                                                | 9.26 ms: 1.56x slower                                      |
| Geometric mean           | (ref)                                                  | 1.32x faster                                               |

Benchmark hidden because not significant (3): mypy2, bench_mp_pool, pickle_list
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: dask, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.05x