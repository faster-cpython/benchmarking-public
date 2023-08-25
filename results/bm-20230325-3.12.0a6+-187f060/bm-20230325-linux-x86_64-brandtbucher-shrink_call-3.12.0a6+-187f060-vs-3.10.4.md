
# Results vs. 3.10.4

- fork: brandtbucher
- ref: shrink_call
- machine: linux-x86_64
- commit hash: 187f060
- commit date: 2023-03-25
- overall geometric mean: 1.30x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230325-linux-x86_64-brandtbucher-shrink_call-3.12.0a6+-187f060 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 251 ms: 1.34x faster                                                |
| chameleon      | 9.06 ms                                                | 6.48 ms: 1.40x faster                                               |
| docutils       | 3.17 sec                                               | 2.56 sec: 1.24x faster                                              |
| html5lib       | 85.9 ms                                                | 61.2 ms: 1.40x faster                                               |
| tornado_http   | 127 ms                                                 | 91.6 ms: 1.39x faster                                               |
| Geometric mean | (ref)                                                  | 1.35x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230325-linux-x86_64-brandtbucher-shrink_call-3.12.0a6+-187f060 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 88.2 ms: 1.61x faster                                               |
| float          | 111 ms                                                 | 74.4 ms: 1.49x faster                                               |
| pidigits       | 190 ms                                                 | 188 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                  | 1.34x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230325-linux-x86_64-brandtbucher-shrink_call-3.12.0a6+-187f060 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 135 ms: 1.31x faster                                                |
| regex_v8       | 25.0 ms                                                | 21.8 ms: 1.15x faster                                               |
| regex_dna      | 222 ms                                                 | 204 ms: 1.09x faster                                                |
| regex_effbot   | 3.23 ms                                                | 3.64 ms: 1.13x slower                                               |
| Geometric mean | (ref)                                                  | 1.10x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230325-linux-x86_64-brandtbucher-shrink_call-3.12.0a6+-187f060 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 289 us: 1.58x faster                                                |
| unpickle_pure_python | 300 us                                                 | 202 us: 1.48x faster                                                |
| json_dumps           | 13.5 ms                                                | 9.62 ms: 1.41x faster                                               |
| xml_etree_process    | 74.9 ms                                                | 55.3 ms: 1.35x faster                                               |
| json_loads           | 28.8 us                                                | 24.3 us: 1.19x faster                                               |
| xml_etree_generate   | 94.2 ms                                                | 80.2 ms: 1.17x faster                                               |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.10x faster                                                |
| pickle_list          | 4.56 us                                                | 4.21 us: 1.08x faster                                               |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                                |
| unpickle_list        | 4.82 us                                                | 5.17 us: 1.07x slower                                               |
| pickle_dict          | 27.3 us                                                | 31.5 us: 1.16x slower                                               |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                        |

Benchmark hidden because not significant (2): unpickle, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230325-linux-x86_64-brandtbucher-shrink_call-3.12.0a6+-187f060 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.83 ms: 1.60x faster                                               |
| python_startup_no_site | 5.82 ms                                                | 6.53 ms: 1.12x slower                                               |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230325-linux-x86_64-brandtbucher-shrink_call-3.12.0a6+-187f060 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 10.0 ms: 1.47x faster                                               |
| django_template | 45.9 ms                                                | 32.8 ms: 1.40x faster                                               |
| genshi_text     | 30.3 ms                                                | 21.7 ms: 1.40x faster                                               |
| genshi_xml      | 63.3 ms                                                | 48.6 ms: 1.30x faster                                               |
| Geometric mean  | (ref)                                                  | 1.39x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230325-linux-x86_64-brandtbucher-shrink_call-3.12.0a6+-187f060 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 28.7 ms: 2.67x faster                                               |
| deltablue               | 7.42 ms                                                | 3.23 ms: 2.30x faster                                               |
| logging_silent          | 175 ns                                                 | 94.8 ns: 1.85x faster                                               |
| asyncio_tcp             | 925 ms                                                 | 505 ms: 1.83x faster                                                |
| scimark_sor             | 197 ms                                                 | 111 ms: 1.77x faster                                                |
| richards                | 74.9 ms                                                | 43.4 ms: 1.73x faster                                               |
| raytrace                | 464 ms                                                 | 278 ms: 1.67x faster                                                |
| go                      | 229 ms                                                 | 139 ms: 1.64x faster                                                |
| crypto_pyaes            | 118 ms                                                 | 73.3 ms: 1.62x faster                                               |
| chaos                   | 106 ms                                                 | 66.0 ms: 1.61x faster                                               |
| nbody                   | 142 ms                                                 | 88.2 ms: 1.61x faster                                               |
| scimark_monte_carlo     | 108 ms                                                 | 67.5 ms: 1.60x faster                                               |
| pyflate                 | 673 ms                                                 | 420 ms: 1.60x faster                                                |
| python_startup          | 14.2 ms                                                | 8.83 ms: 1.60x faster                                               |
| spectral_norm           | 150 ms                                                 | 94.7 ms: 1.58x faster                                               |
| pickle_pure_python      | 455 us                                                 | 289 us: 1.58x faster                                                |
| hexiom                  | 9.53 ms                                                | 6.05 ms: 1.57x faster                                               |
| deepcopy_memo           | 52.3 us                                                | 34.1 us: 1.53x faster                                               |
| scimark_lu              | 163 ms                                                 | 108 ms: 1.51x faster                                                |
| float                   | 111 ms                                                 | 74.4 ms: 1.49x faster                                               |
| unpickle_pure_python    | 300 us                                                 | 202 us: 1.48x faster                                                |
| mako                    | 14.8 ms                                                | 10.0 ms: 1.47x faster                                               |
| unpack_sequence         | 64.7 ns                                                | 44.0 ns: 1.47x faster                                               |
| logging_format          | 8.91 us                                                | 6.23 us: 1.43x faster                                               |
| sqlglot_parse           | 2.06 ms                                                | 1.44 ms: 1.43x faster                                               |
| logging_simple          | 8.07 us                                                | 5.68 us: 1.42x faster                                               |
| json_dumps              | 13.5 ms                                                | 9.62 ms: 1.41x faster                                               |
| sqlglot_transpile       | 2.45 ms                                                | 1.74 ms: 1.41x faster                                               |
| html5lib                | 85.9 ms                                                | 61.2 ms: 1.40x faster                                               |
| coroutines              | 31.8 ms                                                | 22.7 ms: 1.40x faster                                               |
| chameleon               | 9.06 ms                                                | 6.48 ms: 1.40x faster                                               |
| django_template         | 45.9 ms                                                | 32.8 ms: 1.40x faster                                               |
| genshi_text             | 30.3 ms                                                | 21.7 ms: 1.40x faster                                               |
| scimark_fft             | 424 ms                                                 | 304 ms: 1.39x faster                                                |
| pprint_pformat          | 1.99 sec                                               | 1.43 sec: 1.39x faster                                              |
| tornado_http            | 127 ms                                                 | 91.6 ms: 1.39x faster                                               |
| async_tree_io           | 1.77 sec                                               | 1.29 sec: 1.37x faster                                              |
| pprint_safe_repr        | 955 ms                                                 | 696 ms: 1.37x faster                                                |
| aiohttp                 | 1.38 ms                                                | 1.01 ms: 1.37x faster                                               |
| async_tree_none         | 717 ms                                                 | 524 ms: 1.37x faster                                                |
| pycparser               | 1.50 sec                                               | 1.11 sec: 1.36x faster                                              |
| xml_etree_process       | 74.9 ms                                                | 55.3 ms: 1.35x faster                                               |
| 2to3                    | 336 ms                                                 | 251 ms: 1.34x faster                                                |
| deepcopy                | 442 us                                                 | 331 us: 1.34x faster                                                |
| gunicorn                | 1.46 ms                                                | 1.09 ms: 1.34x faster                                               |
| thrift                  | 1.03 ms                                                | 780 us: 1.33x faster                                                |
| deepcopy_reduce         | 3.82 us                                                | 2.91 us: 1.31x faster                                               |
| regex_compile           | 177 ms                                                 | 135 ms: 1.31x faster                                                |
| async_tree_memoization  | 854 ms                                                 | 652 ms: 1.31x faster                                                |
| fannkuch                | 486 ms                                                 | 371 ms: 1.31x faster                                                |
| genshi_xml              | 63.3 ms                                                | 48.6 ms: 1.30x faster                                               |
| mypy2                   | 428 ms                                                 | 332 ms: 1.29x faster                                                |
| sqlglot_normalize       | 135 ms                                                 | 105 ms: 1.29x faster                                                |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.24 ms: 1.29x faster                                               |
| async_tree_cpu_io_mixed | 951 ms                                                 | 742 ms: 1.28x faster                                                |
| sqlglot_optimize        | 65.3 ms                                                | 51.4 ms: 1.27x faster                                               |
| docutils                | 3.17 sec                                               | 2.56 sec: 1.24x faster                                              |
| nqueens                 | 100 ms                                                 | 82.3 ms: 1.21x faster                                               |
| sqlalchemy_declarative  | 165 ms                                                 | 136 ms: 1.21x faster                                                |
| sqlalchemy_imperative   | 21.2 ms                                                | 17.5 ms: 1.21x faster                                               |
| bench_thread_pool       | 947 us                                                 | 791 us: 1.20x faster                                                |
| dulwich_log             | 75.9 ms                                                | 63.6 ms: 1.19x faster                                               |
| sympy_integrate         | 24.3 ms                                                | 20.5 ms: 1.19x faster                                               |
| json_loads              | 28.8 us                                                | 24.3 us: 1.19x faster                                               |
| sympy_expand            | 545 ms                                                 | 461 ms: 1.18x faster                                                |
| xml_etree_generate      | 94.2 ms                                                | 80.2 ms: 1.17x faster                                               |
| sympy_str               | 328 ms                                                 | 282 ms: 1.16x faster                                                |
| json                    | 5.42 ms                                                | 4.67 ms: 1.16x faster                                               |
| regex_v8                | 25.0 ms                                                | 21.8 ms: 1.15x faster                                               |
| comprehensions          | 26.8 us                                                | 23.6 us: 1.13x faster                                               |
| pathlib                 | 20.0 ms                                                | 17.7 ms: 1.13x faster                                               |
| create_gc_cycles        | 1.67 ms                                                | 1.48 ms: 1.13x faster                                               |
| djangocms               | 35.9 us                                                | 32.1 us: 1.12x faster                                               |
| sqlite_synth            | 2.93 us                                                | 2.63 us: 1.12x faster                                               |
| sympy_sum               | 185 ms                                                 | 166 ms: 1.11x faster                                                |
| meteor_contest          | 115 ms                                                 | 104 ms: 1.11x faster                                                |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.10x faster                                                |
| regex_dna               | 222 ms                                                 | 204 ms: 1.09x faster                                                |
| gc_traversal            | 3.84 ms                                                | 3.54 ms: 1.09x faster                                               |
| pickle_list             | 4.56 us                                                | 4.21 us: 1.08x faster                                               |
| xml_etree_iterparse     | 111 ms                                                 | 103 ms: 1.08x faster                                                |
| mdp                     | 2.82 sec                                               | 2.68 sec: 1.05x faster                                              |
| async_generators        | 425 ms                                                 | 410 ms: 1.04x faster                                                |
| pidigits                | 190 ms                                                 | 188 ms: 1.01x faster                                                |
| unpickle_list           | 4.82 us                                                | 5.17 us: 1.07x slower                                               |
| python_startup_no_site  | 5.82 ms                                                | 6.53 ms: 1.12x slower                                               |
| regex_effbot            | 3.23 ms                                                | 3.64 ms: 1.13x slower                                               |
| pickle_dict             | 27.3 us                                                | 31.5 us: 1.16x slower                                               |
| dask                    | 423 ms                                                 | 511 ms: 1.21x slower                                                |
| coverage                | 72.8 ms                                                | 96.1 ms: 1.32x slower                                               |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                        |

Benchmark hidden because not significant (4): unpickle, telco, bench_mp_pool, pickle
Ignored benchmarks (6) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.24x
