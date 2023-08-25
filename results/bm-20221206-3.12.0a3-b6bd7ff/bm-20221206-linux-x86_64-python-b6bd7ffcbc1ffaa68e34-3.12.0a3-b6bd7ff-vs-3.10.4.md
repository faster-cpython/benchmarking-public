
# Results vs. 3.10.4

- fork: python
- ref: b6bd7ffcbc1ffaa68e34
- machine: linux-x86_64
- commit hash: b6bd7ff
- commit date: 2022-12-06
- overall geometric mean: 1.29x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-linux-x86_64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 246 ms: 1.37x faster                                                  |
| chameleon      | 9.06 ms                                                | 6.45 ms: 1.41x faster                                                 |
| docutils       | 3.17 sec                                               | 2.57 sec: 1.23x faster                                                |
| html5lib       | 85.9 ms                                                | 59.7 ms: 1.44x faster                                                 |
| Geometric mean | (ref)                                                  | 1.36x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-linux-x86_64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 111 ms                                                 | 73.2 ms: 1.51x faster                                                 |
| nbody          | 142 ms                                                 | 94.0 ms: 1.51x faster                                                 |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.32x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-linux-x86_64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 129 ms: 1.37x faster                                                  |
| regex_v8       | 25.0 ms                                                | 22.3 ms: 1.12x faster                                                 |
| regex_dna      | 222 ms                                                 | 217 ms: 1.02x faster                                                  |
| regex_effbot   | 3.23 ms                                                | 3.63 ms: 1.12x slower                                                 |
| Geometric mean | (ref)                                                  | 1.09x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-linux-x86_64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 282 us: 1.61x faster                                                  |
| unpickle_pure_python | 300 us                                                 | 200 us: 1.50x faster                                                  |
| json_dumps           | 13.5 ms                                                | 9.52 ms: 1.42x faster                                                 |
| xml_etree_process    | 74.9 ms                                                | 53.7 ms: 1.40x faster                                                 |
| xml_etree_generate   | 94.2 ms                                                | 76.9 ms: 1.23x faster                                                 |
| json_loads           | 28.8 us                                                | 23.8 us: 1.21x faster                                                 |
| pickle_list          | 4.56 us                                                | 3.95 us: 1.15x faster                                                 |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                  |
| xml_etree_iterparse  | 111 ms                                                 | 104 ms: 1.07x faster                                                  |
| unpickle             | 14.1 us                                                | 13.3 us: 1.06x faster                                                 |
| pickle               | 10.3 us                                                | 10.1 us: 1.02x faster                                                 |
| unpickle_list        | 4.82 us                                                | 4.97 us: 1.03x slower                                                 |
| pickle_dict          | 27.3 us                                                | 31.5 us: 1.16x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-linux-x86_64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.52 ms: 1.66x faster                                                 |
| python_startup_no_site | 5.82 ms                                                | 6.07 ms: 1.04x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.26x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-linux-x86_64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.43 ms: 1.56x faster                                                 |
| genshi_text     | 30.3 ms                                                | 20.9 ms: 1.45x faster                                                 |
| django_template | 45.9 ms                                                | 33.0 ms: 1.39x faster                                                 |
| genshi_xml      | 63.3 ms                                                | 48.0 ms: 1.32x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                          |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-linux-x86_64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.22 ms: 2.31x faster                                                 |
| logging_silent          | 175 ns                                                 | 90.9 ns: 1.93x faster                                                 |
| scimark_sor             | 197 ms                                                 | 105 ms: 1.87x faster                                                  |
| richards                | 74.9 ms                                                | 42.0 ms: 1.79x faster                                                 |
| go                      | 229 ms                                                 | 136 ms: 1.69x faster                                                  |
| pyflate                 | 673 ms                                                 | 405 ms: 1.66x faster                                                  |
| python_startup          | 14.2 ms                                                | 8.52 ms: 1.66x faster                                                 |
| scimark_monte_carlo     | 108 ms                                                 | 65.4 ms: 1.66x faster                                                 |
| raytrace                | 464 ms                                                 | 281 ms: 1.65x faster                                                  |
| pickle_pure_python      | 455 us                                                 | 282 us: 1.61x faster                                                  |
| chaos                   | 106 ms                                                 | 66.9 ms: 1.59x faster                                                 |
| crypto_pyaes            | 118 ms                                                 | 75.3 ms: 1.57x faster                                                 |
| hexiom                  | 9.53 ms                                                | 6.08 ms: 1.57x faster                                                 |
| mako                    | 14.8 ms                                                | 9.43 ms: 1.56x faster                                                 |
| spectral_norm           | 150 ms                                                 | 96.0 ms: 1.56x faster                                                 |
| scimark_lu              | 163 ms                                                 | 106 ms: 1.54x faster                                                  |
| sqlglot_parse           | 2.06 ms                                                | 1.34 ms: 1.53x faster                                                 |
| deepcopy_memo           | 52.3 us                                                | 34.2 us: 1.53x faster                                                 |
| float                   | 111 ms                                                 | 73.2 ms: 1.51x faster                                                 |
| nbody                   | 142 ms                                                 | 94.0 ms: 1.51x faster                                                 |
| unpack_sequence         | 64.7 ns                                                | 43.1 ns: 1.50x faster                                                 |
| unpickle_pure_python    | 300 us                                                 | 200 us: 1.50x faster                                                  |
| sqlglot_transpile       | 2.45 ms                                                | 1.63 ms: 1.50x faster                                                 |
| genshi_text             | 30.3 ms                                                | 20.9 ms: 1.45x faster                                                 |
| html5lib                | 85.9 ms                                                | 59.7 ms: 1.44x faster                                                 |
| json_dumps              | 13.5 ms                                                | 9.52 ms: 1.42x faster                                                 |
| chameleon               | 9.06 ms                                                | 6.45 ms: 1.41x faster                                                 |
| pprint_pformat          | 1.99 sec                                               | 1.41 sec: 1.40x faster                                                |
| xml_etree_process       | 74.9 ms                                                | 53.7 ms: 1.40x faster                                                 |
| django_template         | 45.9 ms                                                | 33.0 ms: 1.39x faster                                                 |
| pprint_safe_repr        | 955 ms                                                 | 686 ms: 1.39x faster                                                  |
| logging_format          | 8.91 us                                                | 6.41 us: 1.39x faster                                                 |
| thrift                  | 1.03 ms                                                | 751 us: 1.38x faster                                                  |
| logging_simple          | 8.07 us                                                | 5.88 us: 1.37x faster                                                 |
| pycparser               | 1.50 sec                                               | 1.09 sec: 1.37x faster                                                |
| regex_compile           | 177 ms                                                 | 129 ms: 1.37x faster                                                  |
| 2to3                    | 336 ms                                                 | 246 ms: 1.37x faster                                                  |
| scimark_fft             | 424 ms                                                 | 314 ms: 1.35x faster                                                  |
| async_tree_none         | 717 ms                                                 | 536 ms: 1.34x faster                                                  |
| deepcopy                | 442 us                                                 | 332 us: 1.33x faster                                                  |
| async_tree_io           | 1.77 sec                                               | 1.34 sec: 1.33x faster                                                |
| genshi_xml              | 63.3 ms                                                | 48.0 ms: 1.32x faster                                                 |
| mypy2                   | 428 ms                                                 | 329 ms: 1.30x faster                                                  |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.20 ms: 1.30x faster                                                 |
| sqlglot_normalize       | 135 ms                                                 | 105 ms: 1.29x faster                                                  |
| sqlglot_optimize        | 65.3 ms                                                | 50.6 ms: 1.29x faster                                                 |
| deepcopy_reduce         | 3.82 us                                                | 2.97 us: 1.29x faster                                                 |
| async_tree_memoization  | 854 ms                                                 | 665 ms: 1.28x faster                                                  |
| fannkuch                | 486 ms                                                 | 379 ms: 1.28x faster                                                  |
| coroutines              | 31.8 ms                                                | 25.0 ms: 1.27x faster                                                 |
| nqueens                 | 100 ms                                                 | 80.1 ms: 1.25x faster                                                 |
| async_tree_cpu_io_mixed | 951 ms                                                 | 769 ms: 1.24x faster                                                  |
| docutils                | 3.17 sec                                               | 2.57 sec: 1.23x faster                                                |
| xml_etree_generate      | 94.2 ms                                                | 76.9 ms: 1.23x faster                                                 |
| bench_thread_pool       | 947 us                                                 | 778 us: 1.22x faster                                                  |
| dulwich_log             | 75.9 ms                                                | 62.5 ms: 1.21x faster                                                 |
| json_loads              | 28.8 us                                                | 23.8 us: 1.21x faster                                                 |
| async_generators        | 425 ms                                                 | 354 ms: 1.20x faster                                                  |
| sympy_expand            | 545 ms                                                 | 458 ms: 1.19x faster                                                  |
| sympy_integrate         | 24.3 ms                                                | 20.4 ms: 1.19x faster                                                 |
| dask                    | 423 ms                                                 | 360 ms: 1.17x faster                                                  |
| create_gc_cycles        | 1.67 ms                                                | 1.44 ms: 1.16x faster                                                 |
| sympy_str               | 328 ms                                                 | 283 ms: 1.16x faster                                                  |
| json                    | 5.42 ms                                                | 4.67 ms: 1.16x faster                                                 |
| pickle_list             | 4.56 us                                                | 3.95 us: 1.15x faster                                                 |
| comprehensions          | 26.8 us                                                | 23.5 us: 1.14x faster                                                 |
| sqlite_synth            | 2.93 us                                                | 2.58 us: 1.14x faster                                                 |
| mdp                     | 2.82 sec                                               | 2.50 sec: 1.13x faster                                                |
| sympy_sum               | 185 ms                                                 | 164 ms: 1.12x faster                                                  |
| regex_v8                | 25.0 ms                                                | 22.3 ms: 1.12x faster                                                 |
| meteor_contest          | 115 ms                                                 | 104 ms: 1.10x faster                                                  |
| djangocms               | 35.9 us                                                | 32.6 us: 1.10x faster                                                 |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                  |
| pathlib                 | 20.0 ms                                                | 18.3 ms: 1.10x faster                                                 |
| xml_etree_iterparse     | 111 ms                                                 | 104 ms: 1.07x faster                                                  |
| unpickle                | 14.1 us                                                | 13.3 us: 1.06x faster                                                 |
| asyncio_tcp             | 925 ms                                                 | 890 ms: 1.04x faster                                                  |
| regex_dna               | 222 ms                                                 | 217 ms: 1.02x faster                                                  |
| pickle                  | 10.3 us                                                | 10.1 us: 1.02x faster                                                 |
| telco                   | 6.54 ms                                                | 6.46 ms: 1.01x faster                                                 |
| gc_traversal            | 3.84 ms                                                | 3.81 ms: 1.01x faster                                                 |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                                  |
| generators              | 76.8 ms                                                | 79.1 ms: 1.03x slower                                                 |
| unpickle_list           | 4.82 us                                                | 4.97 us: 1.03x slower                                                 |
| python_startup_no_site  | 5.82 ms                                                | 6.07 ms: 1.04x slower                                                 |
| regex_effbot            | 3.23 ms                                                | 3.63 ms: 1.12x slower                                                 |
| pickle_dict             | 27.3 us                                                | 31.5 us: 1.16x slower                                                 |
| coverage                | 72.8 ms                                                | 102 ms: 1.41x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.29x faster                                                          |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (11) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.23x
