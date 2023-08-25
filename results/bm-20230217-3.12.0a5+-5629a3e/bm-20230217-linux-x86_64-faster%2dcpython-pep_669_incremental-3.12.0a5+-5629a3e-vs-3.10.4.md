
# Results vs. 3.10.4

- fork: faster-cpython
- ref: pep_669_incremental
- machine: linux-x86_64
- commit hash: 5629a3e
- commit date: 2023-02-17
- overall geometric mean: 1.33x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230217-linux-x86_64-faster%2dcpython-pep_669_incremental-3.12.0a5+-5629a3e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 244 ms: 1.38x faster                                                            |
| chameleon      | 9.06 ms                                                | 6.33 ms: 1.43x faster                                                           |
| docutils       | 3.17 sec                                               | 2.50 sec: 1.27x faster                                                          |
| html5lib       | 85.9 ms                                                | 59.7 ms: 1.44x faster                                                           |
| tornado_http   | 127 ms                                                 | 93.3 ms: 1.37x faster                                                           |
| Geometric mean | (ref)                                                  | 1.38x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230217-linux-x86_64-faster%2dcpython-pep_669_incremental-3.12.0a5+-5629a3e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 92.4 ms: 1.53x faster                                                           |
| float          | 111 ms                                                 | 72.4 ms: 1.53x faster                                                           |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                                            |
| Geometric mean | (ref)                                                  | 1.33x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230217-linux-x86_64-faster%2dcpython-pep_669_incremental-3.12.0a5+-5629a3e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 125 ms: 1.41x faster                                                            |
| regex_v8       | 25.0 ms                                                | 22.5 ms: 1.11x faster                                                           |
| regex_dna      | 222 ms                                                 | 205 ms: 1.08x faster                                                            |
| regex_effbot   | 3.23 ms                                                | 3.65 ms: 1.13x slower                                                           |
| Geometric mean | (ref)                                                  | 1.11x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230217-linux-x86_64-faster%2dcpython-pep_669_incremental-3.12.0a5+-5629a3e |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 279 us: 1.63x faster                                                            |
| unpickle_pure_python | 300 us                                                 | 193 us: 1.55x faster                                                            |
| json_dumps           | 13.5 ms                                                | 9.37 ms: 1.44x faster                                                           |
| xml_etree_process    | 74.9 ms                                                | 55.0 ms: 1.36x faster                                                           |
| json_loads           | 28.8 us                                                | 23.7 us: 1.22x faster                                                           |
| xml_etree_generate   | 94.2 ms                                                | 80.3 ms: 1.17x faster                                                           |
| xml_etree_iterparse  | 111 ms                                                 | 100 ms: 1.11x faster                                                            |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.11x faster                                                            |
| pickle_list          | 4.56 us                                                | 4.25 us: 1.07x faster                                                           |
| unpickle             | 14.1 us                                                | 13.7 us: 1.03x faster                                                           |
| unpickle_list        | 4.82 us                                                | 5.08 us: 1.05x slower                                                           |
| pickle_dict          | 27.3 us                                                | 30.8 us: 1.13x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                                    |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230217-linux-x86_64-faster%2dcpython-pep_669_incremental-3.12.0a5+-5629a3e |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.97 ms: 1.58x faster                                                           |
| python_startup_no_site | 5.82 ms                                                | 6.52 ms: 1.12x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230217-linux-x86_64-faster%2dcpython-pep_669_incremental-3.12.0a5+-5629a3e |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.76 ms: 1.51x faster                                                           |
| genshi_text     | 30.3 ms                                                | 20.6 ms: 1.48x faster                                                           |
| django_template | 45.9 ms                                                | 33.1 ms: 1.39x faster                                                           |
| genshi_xml      | 63.3 ms                                                | 46.0 ms: 1.38x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                                    |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230217-linux-x86_64-faster%2dcpython-pep_669_incremental-3.12.0a5+-5629a3e |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 30.8 ms: 2.49x faster                                                           |
| deltablue               | 7.42 ms                                                | 3.13 ms: 2.37x faster                                                           |
| logging_silent          | 175 ns                                                 | 93.8 ns: 1.87x faster                                                           |
| scimark_sor             | 197 ms                                                 | 106 ms: 1.86x faster                                                            |
| asyncio_tcp             | 925 ms                                                 | 501 ms: 1.84x faster                                                            |
| richards                | 74.9 ms                                                | 41.9 ms: 1.79x faster                                                           |
| go                      | 229 ms                                                 | 133 ms: 1.72x faster                                                            |
| pyflate                 | 673 ms                                                 | 401 ms: 1.68x faster                                                            |
| scimark_monte_carlo     | 108 ms                                                 | 65.2 ms: 1.66x faster                                                           |
| raytrace                | 464 ms                                                 | 280 ms: 1.65x faster                                                            |
| chaos                   | 106 ms                                                 | 64.5 ms: 1.65x faster                                                           |
| pickle_pure_python      | 455 us                                                 | 279 us: 1.63x faster                                                            |
| crypto_pyaes            | 118 ms                                                 | 72.6 ms: 1.63x faster                                                           |
| spectral_norm           | 150 ms                                                 | 92.7 ms: 1.62x faster                                                           |
| hexiom                  | 9.53 ms                                                | 5.99 ms: 1.59x faster                                                           |
| python_startup          | 14.2 ms                                                | 8.97 ms: 1.58x faster                                                           |
| deepcopy_memo           | 52.3 us                                                | 33.4 us: 1.57x faster                                                           |
| unpickle_pure_python    | 300 us                                                 | 193 us: 1.55x faster                                                            |
| nbody                   | 142 ms                                                 | 92.4 ms: 1.53x faster                                                           |
| unpack_sequence         | 64.7 ns                                                | 42.4 ns: 1.53x faster                                                           |
| float                   | 111 ms                                                 | 72.4 ms: 1.53x faster                                                           |
| scimark_lu              | 163 ms                                                 | 108 ms: 1.51x faster                                                            |
| mako                    | 14.8 ms                                                | 9.76 ms: 1.51x faster                                                           |
| coroutines              | 31.8 ms                                                | 21.1 ms: 1.51x faster                                                           |
| genshi_text             | 30.3 ms                                                | 20.6 ms: 1.48x faster                                                           |
| sqlglot_parse           | 2.06 ms                                                | 1.41 ms: 1.46x faster                                                           |
| json_dumps              | 13.5 ms                                                | 9.37 ms: 1.44x faster                                                           |
| sqlglot_transpile       | 2.45 ms                                                | 1.69 ms: 1.44x faster                                                           |
| pprint_pformat          | 1.99 sec                                               | 1.38 sec: 1.44x faster                                                          |
| html5lib                | 85.9 ms                                                | 59.7 ms: 1.44x faster                                                           |
| chameleon               | 9.06 ms                                                | 6.33 ms: 1.43x faster                                                           |
| pprint_safe_repr        | 955 ms                                                 | 671 ms: 1.42x faster                                                            |
| regex_compile           | 177 ms                                                 | 125 ms: 1.41x faster                                                            |
| logging_simple          | 8.07 us                                                | 5.72 us: 1.41x faster                                                           |
| logging_format          | 8.91 us                                                | 6.33 us: 1.41x faster                                                           |
| scimark_fft             | 424 ms                                                 | 305 ms: 1.39x faster                                                            |
| django_template         | 45.9 ms                                                | 33.1 ms: 1.39x faster                                                           |
| async_tree_none         | 717 ms                                                 | 518 ms: 1.39x faster                                                            |
| aiohttp                 | 1.38 ms                                                | 1000 us: 1.38x faster                                                           |
| genshi_xml              | 63.3 ms                                                | 46.0 ms: 1.38x faster                                                           |
| 2to3                    | 336 ms                                                 | 244 ms: 1.38x faster                                                            |
| gunicorn                | 1.46 ms                                                | 1.06 ms: 1.37x faster                                                           |
| async_tree_io           | 1.77 sec                                               | 1.29 sec: 1.37x faster                                                          |
| tornado_http            | 127 ms                                                 | 93.3 ms: 1.37x faster                                                           |
| fannkuch                | 486 ms                                                 | 356 ms: 1.36x faster                                                            |
| xml_etree_process       | 74.9 ms                                                | 55.0 ms: 1.36x faster                                                           |
| deepcopy                | 442 us                                                 | 325 us: 1.36x faster                                                            |
| thrift                  | 1.03 ms                                                | 761 us: 1.36x faster                                                            |
| pycparser               | 1.50 sec                                               | 1.13 sec: 1.33x faster                                                          |
| deepcopy_reduce         | 3.82 us                                                | 2.90 us: 1.32x faster                                                           |
| mypy2                   | 428 ms                                                 | 325 ms: 1.32x faster                                                            |
| sqlglot_normalize       | 135 ms                                                 | 103 ms: 1.31x faster                                                            |
| async_tree_memoization  | 854 ms                                                 | 655 ms: 1.30x faster                                                            |
| nqueens                 | 100 ms                                                 | 76.9 ms: 1.30x faster                                                           |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.20 ms: 1.30x faster                                                           |
| sqlglot_optimize        | 65.3 ms                                                | 50.6 ms: 1.29x faster                                                           |
| docutils                | 3.17 sec                                               | 2.50 sec: 1.27x faster                                                          |
| async_tree_cpu_io_mixed | 951 ms                                                 | 750 ms: 1.27x faster                                                            |
| sympy_integrate         | 24.3 ms                                                | 19.5 ms: 1.25x faster                                                           |
| dulwich_log             | 75.9 ms                                                | 61.2 ms: 1.24x faster                                                           |
| sympy_str               | 328 ms                                                 | 265 ms: 1.24x faster                                                            |
| sqlalchemy_declarative  | 165 ms                                                 | 135 ms: 1.23x faster                                                            |
| bench_thread_pool       | 947 us                                                 | 779 us: 1.22x faster                                                            |
| json_loads              | 28.8 us                                                | 23.7 us: 1.22x faster                                                           |
| sympy_expand            | 545 ms                                                 | 449 ms: 1.21x faster                                                            |
| sqlalchemy_imperative   | 21.2 ms                                                | 17.6 ms: 1.20x faster                                                           |
| sympy_sum               | 185 ms                                                 | 155 ms: 1.19x faster                                                            |
| xml_etree_generate      | 94.2 ms                                                | 80.3 ms: 1.17x faster                                                           |
| json                    | 5.42 ms                                                | 4.62 ms: 1.17x faster                                                           |
| mdp                     | 2.82 sec                                               | 2.46 sec: 1.15x faster                                                          |
| sqlite_synth            | 2.93 us                                                | 2.59 us: 1.13x faster                                                           |
| create_gc_cycles        | 1.67 ms                                                | 1.48 ms: 1.13x faster                                                           |
| meteor_contest          | 115 ms                                                 | 102 ms: 1.12x faster                                                            |
| regex_v8                | 25.0 ms                                                | 22.5 ms: 1.11x faster                                                           |
| xml_etree_iterparse     | 111 ms                                                 | 100 ms: 1.11x faster                                                            |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.11x faster                                                            |
| djangocms               | 35.9 us                                                | 32.5 us: 1.11x faster                                                           |
| pathlib                 | 20.0 ms                                                | 18.2 ms: 1.10x faster                                                           |
| regex_dna               | 222 ms                                                 | 205 ms: 1.08x faster                                                            |
| pickle_list             | 4.56 us                                                | 4.25 us: 1.07x faster                                                           |
| gc_traversal            | 3.84 ms                                                | 3.59 ms: 1.07x faster                                                           |
| unpickle                | 14.1 us                                                | 13.7 us: 1.03x faster                                                           |
| telco                   | 6.54 ms                                                | 6.38 ms: 1.03x faster                                                           |
| async_generators        | 425 ms                                                 | 422 ms: 1.01x faster                                                            |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                                            |
| unpickle_list           | 4.82 us                                                | 5.08 us: 1.05x slower                                                           |
| python_startup_no_site  | 5.82 ms                                                | 6.52 ms: 1.12x slower                                                           |
| pickle_dict             | 27.3 us                                                | 30.8 us: 1.13x slower                                                           |
| regex_effbot            | 3.23 ms                                                | 3.65 ms: 1.13x slower                                                           |
| coverage                | 72.8 ms                                                | 99.2 ms: 1.36x slower                                                           |
| Geometric mean          | (ref)                                                  | 1.33x faster                                                                    |

Benchmark hidden because not significant (2): bench_mp_pool, pickle
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, comprehensions, dask, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.28x
