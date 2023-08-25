
# Results vs. 3.10.4

- fork: python
- ref: 4ae1a0ecaffe4320fe97
- machine: linux-x86_64
- commit hash: 4ae1a0e
- commit date: 2022-10-25
- overall geometric mean: 1.30x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221025-linux-x86_64-python-4ae1a0ecaffe4320fe97-3.12.0a1-4ae1a0e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 249 ms: 1.35x faster                                                  |
| chameleon      | 9.06 ms                                                | 6.51 ms: 1.39x faster                                                 |
| docutils       | 3.17 sec                                               | 2.52 sec: 1.26x faster                                                |
| html5lib       | 85.9 ms                                                | 59.9 ms: 1.43x faster                                                 |
| tornado_http   | 127 ms                                                 | 93.7 ms: 1.36x faster                                                 |
| Geometric mean | (ref)                                                  | 1.36x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221025-linux-x86_64-python-4ae1a0ecaffe4320fe97-3.12.0a1-4ae1a0e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 111 ms                                                 | 71.4 ms: 1.55x faster                                                 |
| nbody          | 142 ms                                                 | 96.6 ms: 1.47x faster                                                 |
| pidigits       | 190 ms                                                 | 198 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                  | 1.30x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221025-linux-x86_64-python-4ae1a0ecaffe4320fe97-3.12.0a1-4ae1a0e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 127 ms: 1.39x faster                                                  |
| regex_v8       | 25.0 ms                                                | 21.4 ms: 1.17x faster                                                 |
| regex_dna      | 222 ms                                                 | 201 ms: 1.10x faster                                                  |
| regex_effbot   | 3.23 ms                                                | 3.37 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                  | 1.14x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221025-linux-x86_64-python-4ae1a0ecaffe4320fe97-3.12.0a1-4ae1a0e |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 285 us: 1.60x faster                                                  |
| unpickle_pure_python | 300 us                                                 | 202 us: 1.49x faster                                                  |
| json_dumps           | 13.5 ms                                                | 9.36 ms: 1.45x faster                                                 |
| xml_etree_process    | 74.9 ms                                                | 53.4 ms: 1.40x faster                                                 |
| xml_etree_generate   | 94.2 ms                                                | 76.0 ms: 1.24x faster                                                 |
| json_loads           | 28.8 us                                                | 23.5 us: 1.23x faster                                                 |
| xml_etree_parse      | 163 ms                                                 | 145 ms: 1.12x faster                                                  |
| xml_etree_iterparse  | 111 ms                                                 | 101 ms: 1.11x faster                                                  |
| pickle_list          | 4.56 us                                                | 4.19 us: 1.09x faster                                                 |
| unpickle             | 14.1 us                                                | 13.2 us: 1.07x faster                                                 |
| pickle               | 10.3 us                                                | 10.1 us: 1.01x faster                                                 |
| unpickle_list        | 4.82 us                                                | 4.91 us: 1.02x slower                                                 |
| pickle_dict          | 27.3 us                                                | 31.1 us: 1.14x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.19x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221025-linux-x86_64-python-4ae1a0ecaffe4320fe97-3.12.0a1-4ae1a0e |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.42 ms: 1.68x faster                                                 |
| python_startup_no_site | 5.82 ms                                                | 5.93 ms: 1.02x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.28x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221025-linux-x86_64-python-4ae1a0ecaffe4320fe97-3.12.0a1-4ae1a0e |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.64 ms: 1.53x faster                                                 |
| genshi_text     | 30.3 ms                                                | 21.5 ms: 1.41x faster                                                 |
| django_template | 45.9 ms                                                | 33.0 ms: 1.39x faster                                                 |
| genshi_xml      | 63.3 ms                                                | 50.0 ms: 1.27x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.40x faster                                                          |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221025-linux-x86_64-python-4ae1a0ecaffe4320fe97-3.12.0a1-4ae1a0e |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.30 ms: 2.25x faster                                                 |
| logging_silent          | 175 ns                                                 | 91.6 ns: 1.91x faster                                                 |
| scimark_sor             | 197 ms                                                 | 106 ms: 1.86x faster                                                  |
| richards                | 74.9 ms                                                | 42.4 ms: 1.77x faster                                                 |
| go                      | 229 ms                                                 | 135 ms: 1.70x faster                                                  |
| python_startup          | 14.2 ms                                                | 8.42 ms: 1.68x faster                                                 |
| pyflate                 | 673 ms                                                 | 407 ms: 1.65x faster                                                  |
| raytrace                | 464 ms                                                 | 282 ms: 1.64x faster                                                  |
| scimark_monte_carlo     | 108 ms                                                 | 66.6 ms: 1.63x faster                                                 |
| pickle_pure_python      | 455 us                                                 | 285 us: 1.60x faster                                                  |
| crypto_pyaes            | 118 ms                                                 | 74.8 ms: 1.58x faster                                                 |
| chaos                   | 106 ms                                                 | 67.1 ms: 1.58x faster                                                 |
| spectral_norm           | 150 ms                                                 | 95.2 ms: 1.57x faster                                                 |
| hexiom                  | 9.53 ms                                                | 6.11 ms: 1.56x faster                                                 |
| float                   | 111 ms                                                 | 71.4 ms: 1.55x faster                                                 |
| sqlglot_parse           | 2.06 ms                                                | 1.34 ms: 1.54x faster                                                 |
| mako                    | 14.8 ms                                                | 9.64 ms: 1.53x faster                                                 |
| deepcopy_memo           | 52.3 us                                                | 34.4 us: 1.52x faster                                                 |
| scimark_lu              | 163 ms                                                 | 108 ms: 1.50x faster                                                  |
| sqlglot_transpile       | 2.45 ms                                                | 1.63 ms: 1.50x faster                                                 |
| unpickle_pure_python    | 300 us                                                 | 202 us: 1.49x faster                                                  |
| unpack_sequence         | 64.7 ns                                                | 44.1 ns: 1.47x faster                                                 |
| nbody                   | 142 ms                                                 | 96.6 ms: 1.47x faster                                                 |
| json_dumps              | 13.5 ms                                                | 9.36 ms: 1.45x faster                                                 |
| pprint_pformat          | 1.99 sec                                               | 1.38 sec: 1.44x faster                                                |
| pprint_safe_repr        | 955 ms                                                 | 665 ms: 1.44x faster                                                  |
| html5lib                | 85.9 ms                                                | 59.9 ms: 1.43x faster                                                 |
| genshi_text             | 30.3 ms                                                | 21.5 ms: 1.41x faster                                                 |
| xml_etree_process       | 74.9 ms                                                | 53.4 ms: 1.40x faster                                                 |
| logging_format          | 8.91 us                                                | 6.38 us: 1.40x faster                                                 |
| logging_simple          | 8.07 us                                                | 5.80 us: 1.39x faster                                                 |
| chameleon               | 9.06 ms                                                | 6.51 ms: 1.39x faster                                                 |
| django_template         | 45.9 ms                                                | 33.0 ms: 1.39x faster                                                 |
| regex_compile           | 177 ms                                                 | 127 ms: 1.39x faster                                                  |
| thrift                  | 1.03 ms                                                | 746 us: 1.38x faster                                                  |
| aiohttp                 | 1.38 ms                                                | 1.00 ms: 1.38x faster                                                 |
| gunicorn                | 1.46 ms                                                | 1.07 ms: 1.36x faster                                                 |
| tornado_http            | 127 ms                                                 | 93.7 ms: 1.36x faster                                                 |
| scimark_fft             | 424 ms                                                 | 312 ms: 1.36x faster                                                  |
| async_tree_none         | 717 ms                                                 | 529 ms: 1.36x faster                                                  |
| 2to3                    | 336 ms                                                 | 249 ms: 1.35x faster                                                  |
| pycparser               | 1.50 sec                                               | 1.12 sec: 1.34x faster                                                |
| async_tree_io           | 1.77 sec                                               | 1.33 sec: 1.34x faster                                                |
| deepcopy                | 442 us                                                 | 333 us: 1.33x faster                                                  |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.13 ms: 1.32x faster                                                 |
| deepcopy_reduce         | 3.82 us                                                | 2.91 us: 1.32x faster                                                 |
| fannkuch                | 486 ms                                                 | 370 ms: 1.31x faster                                                  |
| mypy2                   | 428 ms                                                 | 328 ms: 1.31x faster                                                  |
| async_tree_cpu_io_mixed | 951 ms                                                 | 730 ms: 1.30x faster                                                  |
| async_tree_memoization  | 854 ms                                                 | 656 ms: 1.30x faster                                                  |
| sqlglot_normalize       | 135 ms                                                 | 104 ms: 1.30x faster                                                  |
| coroutines              | 31.8 ms                                                | 24.7 ms: 1.29x faster                                                 |
| sqlglot_optimize        | 65.3 ms                                                | 51.2 ms: 1.28x faster                                                 |
| genshi_xml              | 63.3 ms                                                | 50.0 ms: 1.27x faster                                                 |
| docutils                | 3.17 sec                                               | 2.52 sec: 1.26x faster                                                |
| comprehensions          | 26.8 us                                                | 21.3 us: 1.26x faster                                                 |
| nqueens                 | 100 ms                                                 | 80.7 ms: 1.24x faster                                                 |
| xml_etree_generate      | 94.2 ms                                                | 76.0 ms: 1.24x faster                                                 |
| json_loads              | 28.8 us                                                | 23.5 us: 1.23x faster                                                 |
| async_generators        | 425 ms                                                 | 349 ms: 1.22x faster                                                  |
| dulwich_log             | 75.9 ms                                                | 62.4 ms: 1.22x faster                                                 |
| bench_thread_pool       | 947 us                                                 | 780 us: 1.21x faster                                                  |
| sympy_expand            | 545 ms                                                 | 455 ms: 1.20x faster                                                  |
| json                    | 5.42 ms                                                | 4.55 ms: 1.19x faster                                                 |
| sympy_integrate         | 24.3 ms                                                | 20.4 ms: 1.19x faster                                                 |
| dask                    | 423 ms                                                 | 360 ms: 1.17x faster                                                  |
| regex_v8                | 25.0 ms                                                | 21.4 ms: 1.17x faster                                                 |
| sympy_str               | 328 ms                                                 | 283 ms: 1.16x faster                                                  |
| create_gc_cycles        | 1.67 ms                                                | 1.46 ms: 1.15x faster                                                 |
| pylint                  | 525 ms                                                 | 458 ms: 1.15x faster                                                  |
| mdp                     | 2.82 sec                                               | 2.48 sec: 1.14x faster                                                |
| sympy_sum               | 185 ms                                                 | 164 ms: 1.13x faster                                                  |
| xml_etree_parse         | 163 ms                                                 | 145 ms: 1.12x faster                                                  |
| sqlite_synth            | 2.93 us                                                | 2.62 us: 1.12x faster                                                 |
| pathlib                 | 20.0 ms                                                | 17.9 ms: 1.12x faster                                                 |
| xml_etree_iterparse     | 111 ms                                                 | 101 ms: 1.11x faster                                                  |
| djangocms               | 35.9 us                                                | 32.5 us: 1.11x faster                                                 |
| meteor_contest          | 115 ms                                                 | 104 ms: 1.10x faster                                                  |
| regex_dna               | 222 ms                                                 | 201 ms: 1.10x faster                                                  |
| pickle_list             | 4.56 us                                                | 4.19 us: 1.09x faster                                                 |
| gc_traversal            | 3.84 ms                                                | 3.55 ms: 1.08x faster                                                 |
| unpickle                | 14.1 us                                                | 13.2 us: 1.07x faster                                                 |
| asyncio_tcp             | 925 ms                                                 | 890 ms: 1.04x faster                                                  |
| generators              | 76.8 ms                                                | 74.1 ms: 1.04x faster                                                 |
| pickle                  | 10.3 us                                                | 10.1 us: 1.01x faster                                                 |
| bench_mp_pool           | 24.0 ms                                                | 24.0 ms: 1.00x slower                                                 |
| unpickle_list           | 4.82 us                                                | 4.91 us: 1.02x slower                                                 |
| python_startup_no_site  | 5.82 ms                                                | 5.93 ms: 1.02x slower                                                 |
| pidigits                | 190 ms                                                 | 198 ms: 1.04x slower                                                  |
| regex_effbot            | 3.23 ms                                                | 3.37 ms: 1.04x slower                                                 |
| pickle_dict             | 27.3 us                                                | 31.1 us: 1.14x slower                                                 |
| coverage                | 72.8 ms                                                | 102 ms: 1.39x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                          |

Benchmark hidden because not significant (1): telco
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, flaskblogging, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.24x
