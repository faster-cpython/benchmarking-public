
# Results vs. 3.10.4

- fork: ericsnowcurrently
- ref: isolate_dict_next_ke
- machine: linux-x86_64
- commit hash: 145cedf
- commit date: 2023-02-28
- overall geometric mean: 1.29x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_dict_next_ke-3.12.0a5+-145cedf |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 252 ms: 1.34x faster                                                              |
| chameleon      | 9.06 ms                                                | 6.42 ms: 1.41x faster                                                             |
| docutils       | 3.17 sec                                               | 2.55 sec: 1.24x faster                                                            |
| html5lib       | 85.9 ms                                                | 62.5 ms: 1.37x faster                                                             |
| tornado_http   | 127 ms                                                 | 95.2 ms: 1.34x faster                                                             |
| Geometric mean | (ref)                                                  | 1.34x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_dict_next_ke-3.12.0a5+-145cedf |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 93.6 ms: 1.51x faster                                                             |
| float          | 111 ms                                                 | 75.1 ms: 1.47x faster                                                             |
| pidigits       | 190 ms                                                 | 193 ms: 1.02x slower                                                              |
| Geometric mean | (ref)                                                  | 1.30x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_dict_next_ke-3.12.0a5+-145cedf |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 134 ms: 1.32x faster                                                              |
| regex_v8       | 25.0 ms                                                | 21.7 ms: 1.15x faster                                                             |
| regex_dna      | 222 ms                                                 | 200 ms: 1.11x faster                                                              |
| regex_effbot   | 3.23 ms                                                | 3.62 ms: 1.12x slower                                                             |
| Geometric mean | (ref)                                                  | 1.11x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_dict_next_ke-3.12.0a5+-145cedf |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 290 us: 1.57x faster                                                              |
| unpickle_pure_python | 300 us                                                 | 203 us: 1.48x faster                                                              |
| json_dumps           | 13.5 ms                                                | 9.59 ms: 1.41x faster                                                             |
| xml_etree_process    | 74.9 ms                                                | 56.0 ms: 1.34x faster                                                             |
| json_loads           | 28.8 us                                                | 24.2 us: 1.19x faster                                                             |
| xml_etree_generate   | 94.2 ms                                                | 81.8 ms: 1.15x faster                                                             |
| xml_etree_iterparse  | 111 ms                                                 | 100 ms: 1.11x faster                                                              |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                              |
| pickle_list          | 4.56 us                                                | 4.22 us: 1.08x faster                                                             |
| unpickle             | 14.1 us                                                | 13.8 us: 1.02x faster                                                             |
| pickle               | 10.3 us                                                | 10.1 us: 1.01x faster                                                             |
| unpickle_list        | 4.82 us                                                | 5.29 us: 1.10x slower                                                             |
| pickle_dict          | 27.3 us                                                | 31.5 us: 1.16x slower                                                             |
| Geometric mean       | (ref)                                                  | 1.15x faster                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_dict_next_ke-3.12.0a5+-145cedf |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.07 ms: 1.56x faster                                                             |
| python_startup_no_site | 5.82 ms                                                | 6.57 ms: 1.13x slower                                                             |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_dict_next_ke-3.12.0a5+-145cedf |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 10.0 ms: 1.47x faster                                                             |
| genshi_text     | 30.3 ms                                                | 21.6 ms: 1.40x faster                                                             |
| django_template | 45.9 ms                                                | 33.8 ms: 1.36x faster                                                             |
| genshi_xml      | 63.3 ms                                                | 48.0 ms: 1.32x faster                                                             |
| Geometric mean  | (ref)                                                  | 1.39x faster                                                                      |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_dict_next_ke-3.12.0a5+-145cedf |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 30.8 ms: 2.49x faster                                                             |
| deltablue               | 7.42 ms                                                | 3.25 ms: 2.28x faster                                                             |
| asyncio_tcp             | 925 ms                                                 | 500 ms: 1.85x faster                                                              |
| scimark_sor             | 197 ms                                                 | 107 ms: 1.83x faster                                                              |
| logging_silent          | 175 ns                                                 | 96.0 ns: 1.82x faster                                                             |
| richards                | 74.9 ms                                                | 44.2 ms: 1.70x faster                                                             |
| go                      | 229 ms                                                 | 139 ms: 1.66x faster                                                              |
| crypto_pyaes            | 118 ms                                                 | 73.8 ms: 1.60x faster                                                             |
| chaos                   | 106 ms                                                 | 67.1 ms: 1.58x faster                                                             |
| spectral_norm           | 150 ms                                                 | 94.8 ms: 1.58x faster                                                             |
| raytrace                | 464 ms                                                 | 295 ms: 1.57x faster                                                              |
| pyflate                 | 673 ms                                                 | 429 ms: 1.57x faster                                                              |
| pickle_pure_python      | 455 us                                                 | 290 us: 1.57x faster                                                              |
| python_startup          | 14.2 ms                                                | 9.07 ms: 1.56x faster                                                             |
| hexiom                  | 9.53 ms                                                | 6.16 ms: 1.55x faster                                                             |
| scimark_monte_carlo     | 108 ms                                                 | 70.7 ms: 1.53x faster                                                             |
| nbody                   | 142 ms                                                 | 93.6 ms: 1.51x faster                                                             |
| deepcopy_memo           | 52.3 us                                                | 35.0 us: 1.49x faster                                                             |
| unpack_sequence         | 64.7 ns                                                | 43.6 ns: 1.48x faster                                                             |
| scimark_lu              | 163 ms                                                 | 110 ms: 1.48x faster                                                              |
| unpickle_pure_python    | 300 us                                                 | 203 us: 1.48x faster                                                              |
| mako                    | 14.8 ms                                                | 10.0 ms: 1.47x faster                                                             |
| float                   | 111 ms                                                 | 75.1 ms: 1.47x faster                                                             |
| sqlglot_parse           | 2.06 ms                                                | 1.45 ms: 1.42x faster                                                             |
| chameleon               | 9.06 ms                                                | 6.42 ms: 1.41x faster                                                             |
| json_dumps              | 13.5 ms                                                | 9.59 ms: 1.41x faster                                                             |
| sqlglot_transpile       | 2.45 ms                                                | 1.74 ms: 1.41x faster                                                             |
| genshi_text             | 30.3 ms                                                | 21.6 ms: 1.40x faster                                                             |
| pprint_pformat          | 1.99 sec                                               | 1.41 sec: 1.40x faster                                                            |
| logging_format          | 8.91 us                                                | 6.39 us: 1.39x faster                                                             |
| pprint_safe_repr        | 955 ms                                                 | 685 ms: 1.39x faster                                                              |
| logging_simple          | 8.07 us                                                | 5.86 us: 1.38x faster                                                             |
| html5lib                | 85.9 ms                                                | 62.5 ms: 1.37x faster                                                             |
| async_tree_io           | 1.77 sec                                               | 1.29 sec: 1.37x faster                                                            |
| aiohttp                 | 1.38 ms                                                | 1.01 ms: 1.37x faster                                                             |
| pycparser               | 1.50 sec                                               | 1.10 sec: 1.37x faster                                                            |
| async_tree_none         | 717 ms                                                 | 525 ms: 1.36x faster                                                              |
| coroutines              | 31.8 ms                                                | 23.4 ms: 1.36x faster                                                             |
| django_template         | 45.9 ms                                                | 33.8 ms: 1.36x faster                                                             |
| scimark_fft             | 424 ms                                                 | 312 ms: 1.36x faster                                                              |
| thrift                  | 1.03 ms                                                | 770 us: 1.34x faster                                                              |
| fannkuch                | 486 ms                                                 | 362 ms: 1.34x faster                                                              |
| gunicorn                | 1.46 ms                                                | 1.09 ms: 1.34x faster                                                             |
| tornado_http            | 127 ms                                                 | 95.2 ms: 1.34x faster                                                             |
| xml_etree_process       | 74.9 ms                                                | 56.0 ms: 1.34x faster                                                             |
| 2to3                    | 336 ms                                                 | 252 ms: 1.34x faster                                                              |
| regex_compile           | 177 ms                                                 | 134 ms: 1.32x faster                                                              |
| genshi_xml              | 63.3 ms                                                | 48.0 ms: 1.32x faster                                                             |
| async_tree_memoization  | 854 ms                                                 | 650 ms: 1.32x faster                                                              |
| deepcopy                | 442 us                                                 | 337 us: 1.31x faster                                                              |
| sqlglot_normalize       | 135 ms                                                 | 104 ms: 1.30x faster                                                              |
| mypy2                   | 428 ms                                                 | 334 ms: 1.28x faster                                                              |
| sqlglot_optimize        | 65.3 ms                                                | 51.1 ms: 1.28x faster                                                             |
| deepcopy_reduce         | 3.82 us                                                | 3.00 us: 1.28x faster                                                             |
| async_tree_cpu_io_mixed | 951 ms                                                 | 749 ms: 1.27x faster                                                              |
| docutils                | 3.17 sec                                               | 2.55 sec: 1.24x faster                                                            |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.40 ms: 1.24x faster                                                             |
| nqueens                 | 100 ms                                                 | 81.8 ms: 1.22x faster                                                             |
| dulwich_log             | 75.9 ms                                                | 63.1 ms: 1.20x faster                                                             |
| json_loads              | 28.8 us                                                | 24.2 us: 1.19x faster                                                             |
| sqlalchemy_declarative  | 165 ms                                                 | 139 ms: 1.19x faster                                                              |
| bench_thread_pool       | 947 us                                                 | 799 us: 1.19x faster                                                              |
| json                    | 5.42 ms                                                | 4.58 ms: 1.18x faster                                                             |
| sympy_expand            | 545 ms                                                 | 462 ms: 1.18x faster                                                              |
| sympy_integrate         | 24.3 ms                                                | 20.7 ms: 1.17x faster                                                             |
| sqlalchemy_imperative   | 21.2 ms                                                | 18.0 ms: 1.17x faster                                                             |
| regex_v8                | 25.0 ms                                                | 21.7 ms: 1.15x faster                                                             |
| xml_etree_generate      | 94.2 ms                                                | 81.8 ms: 1.15x faster                                                             |
| sympy_str               | 328 ms                                                 | 287 ms: 1.14x faster                                                              |
| sqlite_synth            | 2.93 us                                                | 2.63 us: 1.12x faster                                                             |
| create_gc_cycles        | 1.67 ms                                                | 1.50 ms: 1.11x faster                                                             |
| regex_dna               | 222 ms                                                 | 200 ms: 1.11x faster                                                              |
| xml_etree_iterparse     | 111 ms                                                 | 100 ms: 1.11x faster                                                              |
| pathlib                 | 20.0 ms                                                | 18.0 ms: 1.11x faster                                                             |
| comprehensions          | 26.8 us                                                | 24.2 us: 1.11x faster                                                             |
| djangocms               | 35.9 us                                                | 32.6 us: 1.10x faster                                                             |
| meteor_contest          | 115 ms                                                 | 104 ms: 1.10x faster                                                              |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                              |
| sympy_sum               | 185 ms                                                 | 169 ms: 1.09x faster                                                              |
| pickle_list             | 4.56 us                                                | 4.22 us: 1.08x faster                                                             |
| mdp                     | 2.82 sec                                               | 2.65 sec: 1.07x faster                                                            |
| telco                   | 6.54 ms                                                | 6.36 ms: 1.03x faster                                                             |
| unpickle                | 14.1 us                                                | 13.8 us: 1.02x faster                                                             |
| pickle                  | 10.3 us                                                | 10.1 us: 1.01x faster                                                             |
| async_generators        | 425 ms                                                 | 423 ms: 1.00x faster                                                              |
| gc_traversal            | 3.84 ms                                                | 3.84 ms: 1.00x faster                                                             |
| pidigits                | 190 ms                                                 | 193 ms: 1.02x slower                                                              |
| unpickle_list           | 4.82 us                                                | 5.29 us: 1.10x slower                                                             |
| regex_effbot            | 3.23 ms                                                | 3.62 ms: 1.12x slower                                                             |
| python_startup_no_site  | 5.82 ms                                                | 6.57 ms: 1.13x slower                                                             |
| pickle_dict             | 27.3 us                                                | 31.5 us: 1.16x slower                                                             |
| dask                    | 423 ms                                                 | 509 ms: 1.20x slower                                                              |
| coverage                | 72.8 ms                                                | 95.0 ms: 1.31x slower                                                             |
| Geometric mean          | (ref)                                                  | 1.29x faster                                                                      |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (6) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.24x
