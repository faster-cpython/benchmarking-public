
# Results vs. 3.10.4

- fork: iritkatriel
- ref: int_float_freelist
- machine: linux-x86_64
- commit hash: 42ee27f
- commit date: 2023-02-07
- overall geometric mean: 1.31x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-iritkatriel-int_float_freelist-3.12.0a4+-42ee27f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 252 ms: 1.34x faster                                                      |
| chameleon      | 9.06 ms                                                | 6.31 ms: 1.43x faster                                                     |
| docutils       | 3.17 sec                                               | 2.49 sec: 1.27x faster                                                    |
| html5lib       | 85.9 ms                                                | 60.6 ms: 1.42x faster                                                     |
| tornado_http   | 127 ms                                                 | 94.0 ms: 1.36x faster                                                     |
| Geometric mean | (ref)                                                  | 1.36x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-iritkatriel-int_float_freelist-3.12.0a4+-42ee27f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 111 ms                                                 | 72.5 ms: 1.52x faster                                                     |
| nbody          | 142 ms                                                 | 97.7 ms: 1.45x faster                                                     |
| pidigits       | 190 ms                                                 | 203 ms: 1.07x slower                                                      |
| Geometric mean | (ref)                                                  | 1.27x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-iritkatriel-int_float_freelist-3.12.0a4+-42ee27f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 129 ms: 1.37x faster                                                      |
| regex_v8       | 25.0 ms                                                | 21.8 ms: 1.15x faster                                                     |
| regex_dna      | 222 ms                                                 | 213 ms: 1.04x faster                                                      |
| regex_effbot   | 3.23 ms                                                | 3.43 ms: 1.06x slower                                                     |
| Geometric mean | (ref)                                                  | 1.11x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-iritkatriel-int_float_freelist-3.12.0a4+-42ee27f |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 284 us: 1.60x faster                                                      |
| unpickle_pure_python | 300 us                                                 | 197 us: 1.52x faster                                                      |
| json_dumps           | 13.5 ms                                                | 9.43 ms: 1.44x faster                                                     |
| xml_etree_process    | 74.9 ms                                                | 53.6 ms: 1.40x faster                                                     |
| json_loads           | 28.8 us                                                | 23.7 us: 1.22x faster                                                     |
| xml_etree_generate   | 94.2 ms                                                | 77.9 ms: 1.21x faster                                                     |
| pickle_list          | 4.56 us                                                | 3.98 us: 1.14x faster                                                     |
| xml_etree_parse      | 163 ms                                                 | 147 ms: 1.11x faster                                                      |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.09x faster                                                      |
| unpickle             | 14.1 us                                                | 13.0 us: 1.09x faster                                                     |
| pickle               | 10.3 us                                                | 9.98 us: 1.03x faster                                                     |
| unpickle_list        | 4.82 us                                                | 4.84 us: 1.00x slower                                                     |
| pickle_dict          | 27.3 us                                                | 30.8 us: 1.13x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.19x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-iritkatriel-int_float_freelist-3.12.0a4+-42ee27f |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.97 ms: 1.58x faster                                                     |
| python_startup_no_site | 5.82 ms                                                | 6.49 ms: 1.12x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-iritkatriel-int_float_freelist-3.12.0a4+-42ee27f |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.63 ms: 1.53x faster                                                     |
| genshi_text     | 30.3 ms                                                | 20.5 ms: 1.48x faster                                                     |
| django_template | 45.9 ms                                                | 32.2 ms: 1.43x faster                                                     |
| genshi_xml      | 63.3 ms                                                | 47.5 ms: 1.33x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                              |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-iritkatriel-int_float_freelist-3.12.0a4+-42ee27f |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.21 ms: 2.31x faster                                                     |
| logging_silent          | 175 ns                                                 | 90.7 ns: 1.93x faster                                                     |
| asyncio_tcp             | 925 ms                                                 | 493 ms: 1.88x faster                                                      |
| scimark_sor             | 197 ms                                                 | 107 ms: 1.85x faster                                                      |
| richards                | 74.9 ms                                                | 41.4 ms: 1.81x faster                                                     |
| pyflate                 | 673 ms                                                 | 394 ms: 1.71x faster                                                      |
| go                      | 229 ms                                                 | 135 ms: 1.70x faster                                                      |
| chaos                   | 106 ms                                                 | 63.9 ms: 1.66x faster                                                     |
| raytrace                | 464 ms                                                 | 284 ms: 1.63x faster                                                      |
| pickle_pure_python      | 455 us                                                 | 284 us: 1.60x faster                                                      |
| scimark_monte_carlo     | 108 ms                                                 | 67.7 ms: 1.60x faster                                                     |
| hexiom                  | 9.53 ms                                                | 5.96 ms: 1.60x faster                                                     |
| spectral_norm           | 150 ms                                                 | 94.4 ms: 1.59x faster                                                     |
| python_startup          | 14.2 ms                                                | 8.97 ms: 1.58x faster                                                     |
| crypto_pyaes            | 118 ms                                                 | 75.9 ms: 1.56x faster                                                     |
| unpack_sequence         | 64.7 ns                                                | 42.1 ns: 1.54x faster                                                     |
| mako                    | 14.8 ms                                                | 9.63 ms: 1.53x faster                                                     |
| deepcopy_memo           | 52.3 us                                                | 34.2 us: 1.53x faster                                                     |
| unpickle_pure_python    | 300 us                                                 | 197 us: 1.52x faster                                                      |
| float                   | 111 ms                                                 | 72.5 ms: 1.52x faster                                                     |
| scimark_lu              | 163 ms                                                 | 108 ms: 1.51x faster                                                      |
| genshi_text             | 30.3 ms                                                | 20.5 ms: 1.48x faster                                                     |
| sqlglot_parse           | 2.06 ms                                                | 1.41 ms: 1.46x faster                                                     |
| nbody                   | 142 ms                                                 | 97.7 ms: 1.45x faster                                                     |
| sqlglot_transpile       | 2.45 ms                                                | 1.70 ms: 1.44x faster                                                     |
| json_dumps              | 13.5 ms                                                | 9.43 ms: 1.44x faster                                                     |
| chameleon               | 9.06 ms                                                | 6.31 ms: 1.43x faster                                                     |
| logging_simple          | 8.07 us                                                | 5.64 us: 1.43x faster                                                     |
| django_template         | 45.9 ms                                                | 32.2 ms: 1.43x faster                                                     |
| logging_format          | 8.91 us                                                | 6.26 us: 1.42x faster                                                     |
| html5lib                | 85.9 ms                                                | 60.6 ms: 1.42x faster                                                     |
| pprint_pformat          | 1.99 sec                                               | 1.40 sec: 1.42x faster                                                    |
| pprint_safe_repr        | 955 ms                                                 | 680 ms: 1.40x faster                                                      |
| xml_etree_process       | 74.9 ms                                                | 53.6 ms: 1.40x faster                                                     |
| thrift                  | 1.03 ms                                                | 740 us: 1.40x faster                                                      |
| aiohttp                 | 1.38 ms                                                | 995 us: 1.39x faster                                                      |
| scimark_fft             | 424 ms                                                 | 308 ms: 1.38x faster                                                      |
| regex_compile           | 177 ms                                                 | 129 ms: 1.37x faster                                                      |
| scimark_sparse_mat_mult | 5.45 ms                                                | 3.99 ms: 1.37x faster                                                     |
| gunicorn                | 1.46 ms                                                | 1.07 ms: 1.36x faster                                                     |
| pycparser               | 1.50 sec                                               | 1.10 sec: 1.36x faster                                                    |
| async_tree_none         | 717 ms                                                 | 527 ms: 1.36x faster                                                      |
| tornado_http            | 127 ms                                                 | 94.0 ms: 1.36x faster                                                     |
| async_tree_io           | 1.77 sec                                               | 1.32 sec: 1.35x faster                                                    |
| deepcopy                | 442 us                                                 | 331 us: 1.34x faster                                                      |
| 2to3                    | 336 ms                                                 | 252 ms: 1.34x faster                                                      |
| genshi_xml              | 63.3 ms                                                | 47.5 ms: 1.33x faster                                                     |
| deepcopy_reduce         | 3.82 us                                                | 2.91 us: 1.31x faster                                                     |
| async_tree_memoization  | 854 ms                                                 | 660 ms: 1.30x faster                                                      |
| coroutines              | 31.8 ms                                                | 24.6 ms: 1.29x faster                                                     |
| fannkuch                | 486 ms                                                 | 377 ms: 1.29x faster                                                      |
| sqlglot_optimize        | 65.3 ms                                                | 51.0 ms: 1.28x faster                                                     |
| sqlglot_normalize       | 135 ms                                                 | 106 ms: 1.27x faster                                                      |
| docutils                | 3.17 sec                                               | 2.49 sec: 1.27x faster                                                    |
| nqueens                 | 100 ms                                                 | 78.6 ms: 1.27x faster                                                     |
| async_tree_cpu_io_mixed | 951 ms                                                 | 761 ms: 1.25x faster                                                      |
| sympy_integrate         | 24.3 ms                                                | 19.8 ms: 1.22x faster                                                     |
| dulwich_log             | 75.9 ms                                                | 62.1 ms: 1.22x faster                                                     |
| json_loads              | 28.8 us                                                | 23.7 us: 1.22x faster                                                     |
| bench_thread_pool       | 947 us                                                 | 780 us: 1.22x faster                                                      |
| xml_etree_generate      | 94.2 ms                                                | 77.9 ms: 1.21x faster                                                     |
| sympy_str               | 328 ms                                                 | 272 ms: 1.21x faster                                                      |
| async_generators        | 425 ms                                                 | 353 ms: 1.21x faster                                                      |
| sympy_expand            | 545 ms                                                 | 457 ms: 1.19x faster                                                      |
| json                    | 5.42 ms                                                | 4.56 ms: 1.19x faster                                                     |
| sympy_sum               | 185 ms                                                 | 157 ms: 1.18x faster                                                      |
| mdp                     | 2.82 sec                                               | 2.45 sec: 1.15x faster                                                    |
| regex_v8                | 25.0 ms                                                | 21.8 ms: 1.15x faster                                                     |
| pickle_list             | 4.56 us                                                | 3.98 us: 1.14x faster                                                     |
| sqlite_synth            | 2.93 us                                                | 2.57 us: 1.14x faster                                                     |
| pathlib                 | 20.0 ms                                                | 17.6 ms: 1.14x faster                                                     |
| create_gc_cycles        | 1.67 ms                                                | 1.48 ms: 1.13x faster                                                     |
| djangocms               | 35.9 us                                                | 32.3 us: 1.11x faster                                                     |
| xml_etree_parse         | 163 ms                                                 | 147 ms: 1.11x faster                                                      |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.09x faster                                                      |
| meteor_contest          | 115 ms                                                 | 106 ms: 1.09x faster                                                      |
| unpickle                | 14.1 us                                                | 13.0 us: 1.09x faster                                                     |
| gc_traversal            | 3.84 ms                                                | 3.59 ms: 1.07x faster                                                     |
| regex_dna               | 222 ms                                                 | 213 ms: 1.04x faster                                                      |
| pickle                  | 10.3 us                                                | 9.98 us: 1.03x faster                                                     |
| telco                   | 6.54 ms                                                | 6.42 ms: 1.02x faster                                                     |
| generators              | 76.8 ms                                                | 77.0 ms: 1.00x slower                                                     |
| unpickle_list           | 4.82 us                                                | 4.84 us: 1.00x slower                                                     |
| regex_effbot            | 3.23 ms                                                | 3.43 ms: 1.06x slower                                                     |
| pidigits                | 190 ms                                                 | 203 ms: 1.07x slower                                                      |
| python_startup_no_site  | 5.82 ms                                                | 6.49 ms: 1.12x slower                                                     |
| pickle_dict             | 27.3 us                                                | 30.8 us: 1.13x slower                                                     |
| dask                    | 423 ms                                                 | 495 ms: 1.17x slower                                                      |
| coverage                | 72.8 ms                                                | 97.1 ms: 1.33x slower                                                     |
| Geometric mean          | (ref)                                                  | 1.31x faster                                                              |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230207-3.12.0a4+-42ee27f/bm-20230207-linux-x86_64-iritkatriel-int_float_freelist-3.12.0a4+-42ee27f.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.26x
