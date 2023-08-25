
# Results vs. 3.10.4

- fork: python
- ref: e95dd40aff35775efce4
- machine: linux-x86_64
- commit hash: e95dd40
- commit date: 2023-05-03
- overall geometric mean: 1.24x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230503-linux-x86_64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 271 ms: 1.24x faster                                                   |
| docutils       | 3.17 sec                                               | 2.73 sec: 1.16x faster                                                 |
| tornado_http   | 127 ms                                                 | 99.5 ms: 1.28x faster                                                  |
| Geometric mean | (ref)                                                  | 1.23x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230503-linux-x86_64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 87.5 ms: 1.62x faster                                                  |
| float          | 111 ms                                                 | 83.2 ms: 1.33x faster                                                  |
| pidigits       | 190 ms                                                 | 197 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                  | 1.27x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230503-linux-x86_64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 145 ms: 1.22x faster                                                   |
| regex_v8       | 25.0 ms                                                | 22.1 ms: 1.13x faster                                                  |
| regex_dna      | 222 ms                                                 | 200 ms: 1.11x faster                                                   |
| regex_effbot   | 3.23 ms                                                | 3.69 ms: 1.14x slower                                                  |
| Geometric mean | (ref)                                                  | 1.08x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230503-linux-x86_64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 313 us: 1.45x faster                                                   |
| unpickle_pure_python | 300 us                                                 | 219 us: 1.37x faster                                                   |
| json_dumps           | 13.5 ms                                                | 9.98 ms: 1.36x faster                                                  |
| xml_etree_process    | 74.9 ms                                                | 59.2 ms: 1.26x faster                                                  |
| json_loads           | 28.8 us                                                | 25.8 us: 1.12x faster                                                  |
| xml_etree_generate   | 94.2 ms                                                | 84.7 ms: 1.11x faster                                                  |
| xml_etree_iterparse  | 111 ms                                                 | 104 ms: 1.07x faster                                                   |
| xml_etree_parse      | 163 ms                                                 | 154 ms: 1.06x faster                                                   |
| pickle_list          | 4.56 us                                                | 4.50 us: 1.01x faster                                                  |
| pickle               | 10.3 us                                                | 10.5 us: 1.02x slower                                                  |
| unpickle_list        | 4.82 us                                                | 5.02 us: 1.04x slower                                                  |
| unpickle             | 14.1 us                                                | 15.0 us: 1.06x slower                                                  |
| pickle_dict          | 27.3 us                                                | 30.7 us: 1.12x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.11x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230503-linux-x86_64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.20 ms: 1.54x faster                                                  |
| python_startup_no_site | 5.82 ms                                                | 6.73 ms: 1.16x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.15x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230503-linux-x86_64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|-----------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.7 ms: 1.38x faster                                                  |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230503-linux-x86_64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 31.4 ms: 2.44x faster                                                  |
| deltablue               | 7.42 ms                                                | 3.52 ms: 2.11x faster                                                  |
| asyncio_tcp             | 925 ms                                                 | 506 ms: 1.83x faster                                                   |
| logging_silent          | 175 ns                                                 | 101 ns: 1.74x faster                                                   |
| go                      | 229 ms                                                 | 136 ms: 1.69x faster                                                   |
| richards                | 74.9 ms                                                | 45.0 ms: 1.66x faster                                                  |
| nbody                   | 142 ms                                                 | 87.5 ms: 1.62x faster                                                  |
| scimark_sor             | 197 ms                                                 | 124 ms: 1.59x faster                                                   |
| hexiom                  | 9.53 ms                                                | 6.18 ms: 1.54x faster                                                  |
| python_startup          | 14.2 ms                                                | 9.20 ms: 1.54x faster                                                  |
| raytrace                | 464 ms                                                 | 303 ms: 1.53x faster                                                   |
| sqlglot_parse           | 2.06 ms                                                | 1.35 ms: 1.52x faster                                                  |
| crypto_pyaes            | 118 ms                                                 | 78.0 ms: 1.52x faster                                                  |
| chaos                   | 106 ms                                                 | 70.4 ms: 1.51x faster                                                  |
| pyflate                 | 673 ms                                                 | 451 ms: 1.49x faster                                                   |
| scimark_monte_carlo     | 108 ms                                                 | 73.6 ms: 1.47x faster                                                  |
| async_tree_io           | 1.77 sec                                               | 1.22 sec: 1.46x faster                                                 |
| sqlglot_transpile       | 2.45 ms                                                | 1.68 ms: 1.46x faster                                                  |
| pickle_pure_python      | 455 us                                                 | 313 us: 1.45x faster                                                   |
| async_tree_none         | 717 ms                                                 | 497 ms: 1.44x faster                                                   |
| scimark_lu              | 163 ms                                                 | 113 ms: 1.44x faster                                                   |
| async_tree_memoization  | 854 ms                                                 | 604 ms: 1.41x faster                                                   |
| spectral_norm           | 150 ms                                                 | 108 ms: 1.39x faster                                                   |
| mako                    | 14.8 ms                                                | 10.7 ms: 1.38x faster                                                  |
| unpickle_pure_python    | 300 us                                                 | 219 us: 1.37x faster                                                   |
| deepcopy_memo           | 52.3 us                                                | 38.5 us: 1.36x faster                                                  |
| json_dumps              | 13.5 ms                                                | 9.98 ms: 1.36x faster                                                  |
| coroutines              | 31.8 ms                                                | 23.7 ms: 1.34x faster                                                  |
| pprint_pformat          | 1.99 sec                                               | 1.49 sec: 1.33x faster                                                 |
| float                   | 111 ms                                                 | 83.2 ms: 1.33x faster                                                  |
| async_tree_cpu_io_mixed | 951 ms                                                 | 719 ms: 1.32x faster                                                   |
| pycparser               | 1.50 sec                                               | 1.14 sec: 1.32x faster                                                 |
| pprint_safe_repr        | 955 ms                                                 | 732 ms: 1.30x faster                                                   |
| tornado_http            | 127 ms                                                 | 99.5 ms: 1.28x faster                                                  |
| fannkuch                | 486 ms                                                 | 380 ms: 1.28x faster                                                   |
| logging_simple          | 8.07 us                                                | 6.34 us: 1.27x faster                                                  |
| unpack_sequence         | 64.7 ns                                                | 51.1 ns: 1.27x faster                                                  |
| xml_etree_process       | 74.9 ms                                                | 59.2 ms: 1.26x faster                                                  |
| logging_format          | 8.91 us                                                | 7.06 us: 1.26x faster                                                  |
| 2to3                    | 336 ms                                                 | 271 ms: 1.24x faster                                                   |
| nqueens                 | 100 ms                                                 | 80.9 ms: 1.24x faster                                                  |
| mypy2                   | 428 ms                                                 | 351 ms: 1.22x faster                                                   |
| regex_compile           | 177 ms                                                 | 145 ms: 1.22x faster                                                   |
| deepcopy                | 442 us                                                 | 368 us: 1.20x faster                                                   |
| sqlglot_normalize       | 135 ms                                                 | 113 ms: 1.20x faster                                                   |
| deepcopy_reduce         | 3.82 us                                                | 3.22 us: 1.19x faster                                                  |
| sqlglot_optimize        | 65.3 ms                                                | 55.5 ms: 1.18x faster                                                  |
| docutils                | 3.17 sec                                               | 2.73 sec: 1.16x faster                                                 |
| scimark_fft             | 424 ms                                                 | 367 ms: 1.15x faster                                                   |
| comprehensions          | 26.8 us                                                | 23.3 us: 1.15x faster                                                  |
| regex_v8                | 25.0 ms                                                | 22.1 ms: 1.13x faster                                                  |
| bench_thread_pool       | 947 us                                                 | 838 us: 1.13x faster                                                   |
| sqlalchemy_declarative  | 165 ms                                                 | 147 ms: 1.13x faster                                                   |
| create_gc_cycles        | 1.67 ms                                                | 1.49 ms: 1.12x faster                                                  |
| sqlalchemy_imperative   | 21.2 ms                                                | 18.9 ms: 1.12x faster                                                  |
| json_loads              | 28.8 us                                                | 25.8 us: 1.12x faster                                                  |
| xml_etree_generate      | 94.2 ms                                                | 84.7 ms: 1.11x faster                                                  |
| dulwich_log             | 75.9 ms                                                | 68.3 ms: 1.11x faster                                                  |
| regex_dna               | 222 ms                                                 | 200 ms: 1.11x faster                                                   |
| scimark_sparse_mat_mult | 5.45 ms                                                | 5.01 ms: 1.09x faster                                                  |
| pathlib                 | 20.0 ms                                                | 18.5 ms: 1.08x faster                                                  |
| json                    | 5.42 ms                                                | 5.01 ms: 1.08x faster                                                  |
| sqlite_synth            | 2.93 us                                                | 2.72 us: 1.08x faster                                                  |
| xml_etree_iterparse     | 111 ms                                                 | 104 ms: 1.07x faster                                                   |
| xml_etree_parse         | 163 ms                                                 | 154 ms: 1.06x faster                                                   |
| mdp                     | 2.82 sec                                               | 2.75 sec: 1.03x faster                                                 |
| meteor_contest          | 115 ms                                                 | 113 ms: 1.02x faster                                                   |
| pickle_list             | 4.56 us                                                | 4.50 us: 1.01x faster                                                  |
| pickle                  | 10.3 us                                                | 10.5 us: 1.02x slower                                                  |
| telco                   | 6.54 ms                                                | 6.73 ms: 1.03x slower                                                  |
| gc_traversal            | 3.84 ms                                                | 3.97 ms: 1.03x slower                                                  |
| pidigits                | 190 ms                                                 | 197 ms: 1.04x slower                                                   |
| unpickle_list           | 4.82 us                                                | 5.02 us: 1.04x slower                                                  |
| async_generators        | 425 ms                                                 | 446 ms: 1.05x slower                                                   |
| unpickle                | 14.1 us                                                | 15.0 us: 1.06x slower                                                  |
| pickle_dict             | 27.3 us                                                | 30.7 us: 1.12x slower                                                  |
| regex_effbot            | 3.23 ms                                                | 3.69 ms: 1.14x slower                                                  |
| python_startup_no_site  | 5.82 ms                                                | 6.73 ms: 1.16x slower                                                  |
| dask                    | 423 ms                                                 | 540 ms: 1.28x slower                                                   |
| coverage                | 72.8 ms                                                | 103 ms: 1.41x slower                                                   |
| Geometric mean          | (ref)                                                  | 1.24x faster                                                           |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (19) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, richards_super, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.17x
