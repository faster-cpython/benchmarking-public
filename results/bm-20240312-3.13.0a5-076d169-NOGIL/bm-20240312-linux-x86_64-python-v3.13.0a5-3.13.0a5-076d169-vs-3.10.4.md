# Results vs. 3.10.4

- fork: python
- ref: v3.13.0a5
- machine: linux-x86_64
- commit hash: 076d169
- commit date: 2024-03-12
- overall geometric mean: 1.09x slower
- HPT reliability: 99.97%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 377 ms: 1.08x slower                                       |
| chameleon      | 9.68 ms                                                | 12.3 ms: 1.27x slower                                      |
| docutils       | 3.30 sec                                               | 3.28 sec: 1.01x faster                                     |
| html5lib       | 88.9 ms                                                | 91.5 ms: 1.03x slower                                      |
| Geometric mean | (ref)                                                  | 1.07x slower                                               |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 877 ms: 2.02x faster                                       |
| async_tree_none         | 728 ms                                                 | 412 ms: 1.77x faster                                       |
| async_tree_memoization  | 870 ms                                                 | 518 ms: 1.68x faster                                       |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 668 ms: 1.52x faster                                       |
| Geometric mean          | (ref)                                                  | 1.74x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 191 ms                                                 | 192 ms: 1.00x slower                                       |
| float          | 117 ms                                                 | 127 ms: 1.08x slower                                       |
| nbody          | 154 ms                                                 | 215 ms: 1.40x slower                                       |
| Geometric mean | (ref)                                                  | 1.15x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_v8       | 27.8 ms                                                | 26.9 ms: 1.03x faster                                      |
| regex_effbot   | 3.63 ms                                                | 3.56 ms: 1.02x faster                                      |
| regex_dna      | 227 ms                                                 | 230 ms: 1.01x slower                                       |
| regex_compile  | 188 ms                                                 | 204 ms: 1.08x slower                                       |
| Geometric mean | (ref)                                                  | 1.01x slower                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| xml_etree_parse      | 168 ms                                                 | 156 ms: 1.08x faster                                       |
| json_dumps           | 14.2 ms                                                | 13.7 ms: 1.03x faster                                      |
| pickle_list          | 5.08 us                                                | 4.97 us: 1.02x faster                                      |
| tomli_loads          | 3.14 sec                                               | 3.11 sec: 1.01x faster                                     |
| xml_etree_iterparse  | 115 ms                                                 | 117 ms: 1.02x slower                                       |
| xml_etree_generate   | 99.4 ms                                                | 108 ms: 1.08x slower                                       |
| pickle_pure_python   | 484 us                                                 | 528 us: 1.09x slower                                       |
| xml_etree_process    | 79.1 ms                                                | 86.4 ms: 1.09x slower                                      |
| unpickle_list        | 5.20 us                                                | 5.75 us: 1.11x slower                                      |
| unpickle_pure_python | 331 us                                                 | 367 us: 1.11x slower                                       |
| json_loads           | 31.2 us                                                | 34.8 us: 1.12x slower                                      |
| pickle               | 10.7 us                                                | 12.1 us: 1.13x slower                                      |
| unpickle             | 14.4 us                                                | 18.1 us: 1.26x slower                                      |
| pickle_dict          | 29.6 us                                                | 41.4 us: 1.40x slower                                      |
| Geometric mean       | (ref)                                                  | 1.08x slower                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.6 ms: 1.07x faster                                      |
| python_startup_no_site | 5.93 ms                                                | 11.6 ms: 1.95x slower                                      |
| Geometric mean         | (ref)                                                  | 1.35x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| genshi_xml      | 66.0 ms                                                | 78.4 ms: 1.19x slower                                      |
| django_template | 48.2 ms                                                | 57.7 ms: 1.20x slower                                      |
| genshi_text     | 31.8 ms                                                | 38.9 ms: 1.22x slower                                      |
| mako            | 16.3 ms                                                | 21.0 ms: 1.29x slower                                      |
| Geometric mean  | (ref)                                                  | 1.22x slower                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 167 us: 3.26x faster                                       |
| generators               | 80.1 ms                                                | 36.2 ms: 2.21x faster                                      |
| async_tree_io            | 1.77 sec                                               | 877 ms: 2.02x faster                                       |
| async_tree_none          | 728 ms                                                 | 412 ms: 1.77x faster                                       |
| async_tree_memoization   | 870 ms                                                 | 518 ms: 1.68x faster                                       |
| asyncio_tcp              | 922 ms                                                 | 584 ms: 1.58x faster                                       |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 668 ms: 1.52x faster                                       |
| create_gc_cycles         | 1.62 ms                                                | 1.08 ms: 1.50x faster                                      |
| pylint                   | 551 ms                                                 | 390 ms: 1.41x faster                                       |
| gc_traversal             | 3.62 ms                                                | 2.57 ms: 1.41x faster                                      |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.99 sec: 1.29x faster                                     |
| coroutines               | 35.1 ms                                                | 29.3 ms: 1.20x faster                                      |
| crypto_pyaes             | 128 ms                                                 | 108 ms: 1.18x faster                                       |
| richards                 | 79.3 ms                                                | 68.0 ms: 1.17x faster                                      |
| richards_super           | 94.7 ms                                                | 82.3 ms: 1.15x faster                                      |
| comprehensions           | 28.8 us                                                | 25.7 us: 1.12x faster                                      |
| xml_etree_parse          | 168 ms                                                 | 156 ms: 1.08x faster                                       |
| logging_silent           | 190 ns                                                 | 176 ns: 1.08x faster                                       |
| python_startup           | 14.6 ms                                                | 13.6 ms: 1.07x faster                                      |
| deltablue                | 7.91 ms                                                | 7.43 ms: 1.06x faster                                      |
| json_dumps               | 14.2 ms                                                | 13.7 ms: 1.03x faster                                      |
| regex_v8                 | 27.8 ms                                                | 26.9 ms: 1.03x faster                                      |
| pickle_list              | 5.08 us                                                | 4.97 us: 1.02x faster                                      |
| regex_effbot             | 3.63 ms                                                | 3.56 ms: 1.02x faster                                      |
| tomli_loads              | 3.14 sec                                               | 3.11 sec: 1.01x faster                                     |
| docutils                 | 3.30 sec                                               | 3.28 sec: 1.01x faster                                     |
| bench_mp_pool            | 24.0 ms                                                | 23.9 ms: 1.01x faster                                      |
| pidigits                 | 191 ms                                                 | 192 ms: 1.00x slower                                       |
| scimark_monte_carlo      | 118 ms                                                 | 119 ms: 1.01x slower                                       |
| regex_dna                | 227 ms                                                 | 230 ms: 1.01x slower                                       |
| asyncio_websockets       | 559 ms                                                 | 567 ms: 1.02x slower                                       |
| xml_etree_iterparse      | 115 ms                                                 | 117 ms: 1.02x slower                                       |
| pyflate                  | 716 ms                                                 | 728 ms: 1.02x slower                                       |
| raytrace                 | 507 ms                                                 | 518 ms: 1.02x slower                                       |
| html5lib                 | 88.9 ms                                                | 91.5 ms: 1.03x slower                                      |
| scimark_fft              | 466 ms                                                 | 481 ms: 1.03x slower                                       |
| deepcopy_memo            | 58.5 us                                                | 60.8 us: 1.04x slower                                      |
| fannkuch                 | 532 ms                                                 | 559 ms: 1.05x slower                                       |
| nqueens                  | 106 ms                                                 | 111 ms: 1.05x slower                                       |
| dulwich_log              | 84.3 ms                                                | 89.2 ms: 1.06x slower                                      |
| hexiom                   | 10.4 ms                                                | 11.0 ms: 1.06x slower                                      |
| spectral_norm            | 170 ms                                                 | 181 ms: 1.06x slower                                       |
| float                    | 117 ms                                                 | 127 ms: 1.08x slower                                       |
| xml_etree_generate       | 99.4 ms                                                | 108 ms: 1.08x slower                                       |
| 2to3                     | 348 ms                                                 | 377 ms: 1.08x slower                                       |
| regex_compile            | 188 ms                                                 | 204 ms: 1.08x slower                                       |
| pickle_pure_python       | 484 us                                                 | 528 us: 1.09x slower                                       |
| xml_etree_process        | 79.1 ms                                                | 86.4 ms: 1.09x slower                                      |
| sqlglot_parse            | 2.17 ms                                                | 2.37 ms: 1.09x slower                                      |
| json                     | 5.69 ms                                                | 6.24 ms: 1.10x slower                                      |
| scimark_sor              | 220 ms                                                 | 241 ms: 1.10x slower                                       |
| deepcopy                 | 479 us                                                 | 527 us: 1.10x slower                                       |
| sympy_integrate          | 25.8 ms                                                | 28.4 ms: 1.10x slower                                      |
| sqlglot_transpile        | 2.57 ms                                                | 2.84 ms: 1.11x slower                                      |
| unpickle_list            | 5.20 us                                                | 5.75 us: 1.11x slower                                      |
| aiohttp                  | 1.44 ms                                                | 1.59 ms: 1.11x slower                                      |
| unpickle_pure_python     | 331 us                                                 | 367 us: 1.11x slower                                       |
| json_loads               | 31.2 us                                                | 34.8 us: 1.12x slower                                      |
| gunicorn                 | 1.53 ms                                                | 1.71 ms: 1.12x slower                                      |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 7.26 ms: 1.12x slower                                      |
| meteor_contest           | 120 ms                                                 | 136 ms: 1.13x slower                                       |
| pickle                   | 10.7 us                                                | 12.1 us: 1.13x slower                                      |
| deepcopy_reduce          | 4.17 us                                                | 4.74 us: 1.14x slower                                      |
| go                       | 240 ms                                                 | 273 ms: 1.14x slower                                       |
| async_generators         | 444 ms                                                 | 511 ms: 1.15x slower                                       |
| mdp                      | 2.85 sec                                               | 3.30 sec: 1.16x slower                                     |
| pprint_safe_repr         | 1.02 sec                                               | 1.20 sec: 1.18x slower                                     |
| pprint_pformat           | 2.10 sec                                               | 2.49 sec: 1.18x slower                                     |
| genshi_xml               | 66.0 ms                                                | 78.4 ms: 1.19x slower                                      |
| django_template          | 48.2 ms                                                | 57.7 ms: 1.20x slower                                      |
| mypy2                    | 894 ms                                                 | 1.07 sec: 1.20x slower                                     |
| sympy_str                | 346 ms                                                 | 421 ms: 1.22x slower                                       |
| genshi_text              | 31.8 ms                                                | 38.9 ms: 1.22x slower                                      |
| logging_simple           | 8.30 us                                                | 10.2 us: 1.22x slower                                      |
| logging_format           | 9.09 us                                                | 11.2 us: 1.23x slower                                      |
| sqlglot_normalize        | 143 ms                                                 | 177 ms: 1.24x slower                                       |
| unpickle                 | 14.4 us                                                | 18.1 us: 1.26x slower                                      |
| pathlib                  | 20.5 ms                                                | 25.9 ms: 1.27x slower                                      |
| chameleon                | 9.68 ms                                                | 12.3 ms: 1.27x slower                                      |
| sqlite_synth             | 3.02 us                                                | 3.84 us: 1.27x slower                                      |
| sqlglot_optimize         | 69.2 ms                                                | 88.8 ms: 1.28x slower                                      |
| mako                     | 16.3 ms                                                | 21.0 ms: 1.29x slower                                      |
| sympy_sum                | 196 ms                                                 | 254 ms: 1.29x slower                                       |
| sympy_expand             | 566 ms                                                 | 740 ms: 1.31x slower                                       |
| pickle_dict              | 29.6 us                                                | 41.4 us: 1.40x slower                                      |
| nbody                    | 154 ms                                                 | 215 ms: 1.40x slower                                       |
| scimark_lu               | 176 ms                                                 | 250 ms: 1.42x slower                                       |
| telco                    | 7.27 ms                                                | 11.7 ms: 1.61x slower                                      |
| flaskblogging            | 8.58 ms                                                | 14.3 ms: 1.67x slower                                      |
| python_startup_no_site   | 5.93 ms                                                | 11.6 ms: 1.95x slower                                      |
| bench_thread_pool        | 986 us                                                 | 3.01 ms: 3.05x slower                                      |
| coverage                 | 79.4 ms                                                | 891 ms: 11.21x slower                                      |
| thrift                   | 1.07 ms                                                | 12.4 ms: 11.56x slower                                     |
| Geometric mean           | (ref)                                                  | 1.09x slower                                               |

Benchmark hidden because not significant (3): chaos, pycparser, tornado_http
Ignored benchmarks (5) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: dask, djangocms, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240312-3.13.0a5-076d169-NOGIL/bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 99.97% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.21x