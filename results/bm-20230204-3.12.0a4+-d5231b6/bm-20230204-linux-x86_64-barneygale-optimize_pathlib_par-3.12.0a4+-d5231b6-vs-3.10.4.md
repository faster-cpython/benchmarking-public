
# Results vs. 3.10.4

- fork: barneygale
- ref: optimize_pathlib_par
- machine: linux-x86_64
- commit hash: d5231b6
- commit date: 2023-02-04
- overall geometric mean: 1.31x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230204-linux-x86_64-barneygale-optimize_pathlib_par-3.12.0a4+-d5231b6 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 252 ms: 1.33x faster                                                       |
| chameleon      | 9.06 ms                                                | 6.27 ms: 1.45x faster                                                      |
| docutils       | 3.17 sec                                               | 2.51 sec: 1.26x faster                                                     |
| html5lib       | 85.9 ms                                                | 60.4 ms: 1.42x faster                                                      |
| tornado_http   | 127 ms                                                 | 93.7 ms: 1.36x faster                                                      |
| Geometric mean | (ref)                                                  | 1.36x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230204-linux-x86_64-barneygale-optimize_pathlib_par-3.12.0a4+-d5231b6 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 111 ms                                                 | 72.2 ms: 1.53x faster                                                      |
| nbody          | 142 ms                                                 | 92.6 ms: 1.53x faster                                                      |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                                       |
| Geometric mean | (ref)                                                  | 1.33x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230204-linux-x86_64-barneygale-optimize_pathlib_par-3.12.0a4+-d5231b6 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 127 ms: 1.39x faster                                                       |
| regex_v8       | 25.0 ms                                                | 22.6 ms: 1.11x faster                                                      |
| regex_dna      | 222 ms                                                 | 216 ms: 1.03x faster                                                       |
| regex_effbot   | 3.23 ms                                                | 3.59 ms: 1.11x slower                                                      |
| Geometric mean | (ref)                                                  | 1.09x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230204-linux-x86_64-barneygale-optimize_pathlib_par-3.12.0a4+-d5231b6 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 280 us: 1.62x faster                                                       |
| unpickle_pure_python | 300 us                                                 | 197 us: 1.52x faster                                                       |
| json_dumps           | 13.5 ms                                                | 9.22 ms: 1.47x faster                                                      |
| xml_etree_process    | 74.9 ms                                                | 54.0 ms: 1.39x faster                                                      |
| xml_etree_generate   | 94.2 ms                                                | 77.7 ms: 1.21x faster                                                      |
| json_loads           | 28.8 us                                                | 23.9 us: 1.20x faster                                                      |
| xml_etree_parse      | 163 ms                                                 | 146 ms: 1.12x faster                                                       |
| pickle_list          | 4.56 us                                                | 4.17 us: 1.09x faster                                                      |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.09x faster                                                       |
| unpickle             | 14.1 us                                                | 13.5 us: 1.04x faster                                                      |
| pickle               | 10.3 us                                                | 10.1 us: 1.02x faster                                                      |
| unpickle_list        | 4.82 us                                                | 4.98 us: 1.03x slower                                                      |
| pickle_dict          | 27.3 us                                                | 30.6 us: 1.12x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230204-linux-x86_64-barneygale-optimize_pathlib_par-3.12.0a4+-d5231b6 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.91 ms: 1.59x faster                                                      |
| python_startup_no_site | 5.82 ms                                                | 6.44 ms: 1.11x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.20x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230204-linux-x86_64-barneygale-optimize_pathlib_par-3.12.0a4+-d5231b6 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.74 ms: 1.51x faster                                                      |
| genshi_text     | 30.3 ms                                                | 20.8 ms: 1.46x faster                                                      |
| django_template | 45.9 ms                                                | 32.6 ms: 1.41x faster                                                      |
| genshi_xml      | 63.3 ms                                                | 46.5 ms: 1.36x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                               |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230204-linux-x86_64-barneygale-optimize_pathlib_par-3.12.0a4+-d5231b6 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.19 ms: 2.32x faster                                                      |
| asyncio_tcp             | 925 ms                                                 | 489 ms: 1.89x faster                                                       |
| logging_silent          | 175 ns                                                 | 94.0 ns: 1.86x faster                                                      |
| scimark_sor             | 197 ms                                                 | 107 ms: 1.84x faster                                                       |
| richards                | 74.9 ms                                                | 42.3 ms: 1.77x faster                                                      |
| pyflate                 | 673 ms                                                 | 397 ms: 1.70x faster                                                       |
| go                      | 229 ms                                                 | 135 ms: 1.70x faster                                                       |
| chaos                   | 106 ms                                                 | 63.6 ms: 1.67x faster                                                      |
| scimark_monte_carlo     | 108 ms                                                 | 65.1 ms: 1.66x faster                                                      |
| raytrace                | 464 ms                                                 | 281 ms: 1.65x faster                                                       |
| pickle_pure_python      | 455 us                                                 | 280 us: 1.62x faster                                                       |
| crypto_pyaes            | 118 ms                                                 | 73.4 ms: 1.61x faster                                                      |
| python_startup          | 14.2 ms                                                | 8.91 ms: 1.59x faster                                                      |
| spectral_norm           | 150 ms                                                 | 94.5 ms: 1.59x faster                                                      |
| hexiom                  | 9.53 ms                                                | 6.03 ms: 1.58x faster                                                      |
| float                   | 111 ms                                                 | 72.2 ms: 1.53x faster                                                      |
| nbody                   | 142 ms                                                 | 92.6 ms: 1.53x faster                                                      |
| unpickle_pure_python    | 300 us                                                 | 197 us: 1.52x faster                                                       |
| deepcopy_memo           | 52.3 us                                                | 34.5 us: 1.52x faster                                                      |
| mako                    | 14.8 ms                                                | 9.74 ms: 1.51x faster                                                      |
| unpack_sequence         | 64.7 ns                                                | 43.1 ns: 1.50x faster                                                      |
| scimark_lu              | 163 ms                                                 | 110 ms: 1.48x faster                                                       |
| json_dumps              | 13.5 ms                                                | 9.22 ms: 1.47x faster                                                      |
| genshi_text             | 30.3 ms                                                | 20.8 ms: 1.46x faster                                                      |
| pprint_pformat          | 1.99 sec                                               | 1.37 sec: 1.45x faster                                                     |
| chameleon               | 9.06 ms                                                | 6.27 ms: 1.45x faster                                                      |
| sqlglot_parse           | 2.06 ms                                                | 1.43 ms: 1.44x faster                                                      |
| pprint_safe_repr        | 955 ms                                                 | 666 ms: 1.43x faster                                                       |
| html5lib                | 85.9 ms                                                | 60.4 ms: 1.42x faster                                                      |
| sqlglot_transpile       | 2.45 ms                                                | 1.72 ms: 1.42x faster                                                      |
| logging_simple          | 8.07 us                                                | 5.72 us: 1.41x faster                                                      |
| django_template         | 45.9 ms                                                | 32.6 ms: 1.41x faster                                                      |
| scimark_fft             | 424 ms                                                 | 302 ms: 1.40x faster                                                       |
| logging_format          | 8.91 us                                                | 6.36 us: 1.40x faster                                                      |
| aiohttp                 | 1.38 ms                                                | 995 us: 1.39x faster                                                       |
| regex_compile           | 177 ms                                                 | 127 ms: 1.39x faster                                                       |
| xml_etree_process       | 74.9 ms                                                | 54.0 ms: 1.39x faster                                                      |
| thrift                  | 1.03 ms                                                | 752 us: 1.38x faster                                                       |
| scimark_sparse_mat_mult | 5.45 ms                                                | 3.99 ms: 1.37x faster                                                      |
| async_tree_none         | 717 ms                                                 | 525 ms: 1.36x faster                                                       |
| genshi_xml              | 63.3 ms                                                | 46.5 ms: 1.36x faster                                                      |
| gunicorn                | 1.46 ms                                                | 1.07 ms: 1.36x faster                                                      |
| tornado_http            | 127 ms                                                 | 93.7 ms: 1.36x faster                                                      |
| async_tree_io           | 1.77 sec                                               | 1.31 sec: 1.36x faster                                                     |
| fannkuch                | 486 ms                                                 | 359 ms: 1.36x faster                                                       |
| deepcopy                | 442 us                                                 | 328 us: 1.35x faster                                                       |
| 2to3                    | 336 ms                                                 | 252 ms: 1.33x faster                                                       |
| async_tree_memoization  | 854 ms                                                 | 654 ms: 1.31x faster                                                       |
| pycparser               | 1.50 sec                                               | 1.15 sec: 1.30x faster                                                     |
| deepcopy_reduce         | 3.82 us                                                | 2.93 us: 1.30x faster                                                      |
| nqueens                 | 100 ms                                                 | 77.0 ms: 1.30x faster                                                      |
| coroutines              | 31.8 ms                                                | 24.8 ms: 1.28x faster                                                      |
| sqlglot_normalize       | 135 ms                                                 | 106 ms: 1.28x faster                                                       |
| sqlglot_optimize        | 65.3 ms                                                | 51.1 ms: 1.28x faster                                                      |
| docutils                | 3.17 sec                                               | 2.51 sec: 1.26x faster                                                     |
| async_tree_cpu_io_mixed | 951 ms                                                 | 757 ms: 1.26x faster                                                       |
| sympy_integrate         | 24.3 ms                                                | 19.8 ms: 1.22x faster                                                      |
| sympy_str               | 328 ms                                                 | 269 ms: 1.22x faster                                                       |
| async_generators        | 425 ms                                                 | 350 ms: 1.21x faster                                                       |
| xml_etree_generate      | 94.2 ms                                                | 77.7 ms: 1.21x faster                                                      |
| dulwich_log             | 75.9 ms                                                | 62.8 ms: 1.21x faster                                                      |
| bench_thread_pool       | 947 us                                                 | 785 us: 1.21x faster                                                       |
| json_loads              | 28.8 us                                                | 23.9 us: 1.20x faster                                                      |
| sympy_expand            | 545 ms                                                 | 456 ms: 1.20x faster                                                       |
| sympy_sum               | 185 ms                                                 | 155 ms: 1.19x faster                                                       |
| json                    | 5.42 ms                                                | 4.63 ms: 1.17x faster                                                      |
| mdp                     | 2.82 sec                                               | 2.44 sec: 1.16x faster                                                     |
| create_gc_cycles        | 1.67 ms                                                | 1.47 ms: 1.14x faster                                                      |
| sqlite_synth            | 2.93 us                                                | 2.61 us: 1.12x faster                                                      |
| djangocms               | 35.9 us                                                | 32.1 us: 1.12x faster                                                      |
| xml_etree_parse         | 163 ms                                                 | 146 ms: 1.12x faster                                                       |
| regex_v8                | 25.0 ms                                                | 22.6 ms: 1.11x faster                                                      |
| meteor_contest          | 115 ms                                                 | 104 ms: 1.10x faster                                                       |
| pickle_list             | 4.56 us                                                | 4.17 us: 1.09x faster                                                      |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.09x faster                                                       |
| gc_traversal            | 3.84 ms                                                | 3.53 ms: 1.09x faster                                                      |
| pathlib                 | 20.0 ms                                                | 19.0 ms: 1.06x faster                                                      |
| unpickle                | 14.1 us                                                | 13.5 us: 1.04x faster                                                      |
| generators              | 76.8 ms                                                | 74.2 ms: 1.03x faster                                                      |
| regex_dna               | 222 ms                                                 | 216 ms: 1.03x faster                                                       |
| pickle                  | 10.3 us                                                | 10.1 us: 1.02x faster                                                      |
| telco                   | 6.54 ms                                                | 6.41 ms: 1.02x faster                                                      |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                                       |
| unpickle_list           | 4.82 us                                                | 4.98 us: 1.03x slower                                                      |
| python_startup_no_site  | 5.82 ms                                                | 6.44 ms: 1.11x slower                                                      |
| regex_effbot            | 3.23 ms                                                | 3.59 ms: 1.11x slower                                                      |
| pickle_dict             | 27.3 us                                                | 30.6 us: 1.12x slower                                                      |
| dask                    | 423 ms                                                 | 498 ms: 1.18x slower                                                       |
| coverage                | 72.8 ms                                                | 95.1 ms: 1.31x slower                                                      |
| Geometric mean          | (ref)                                                  | 1.31x faster                                                               |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230204-3.12.0a4+-d5231b6/bm-20230204-linux-x86_64-barneygale-optimize_pathlib_par-3.12.0a4+-d5231b6.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.26x
