
# Results vs. 3.10.4

- fork: ericsnowcurrently
- ref: per_interpreter_allo
- machine: linux-x86_64
- commit hash: 299527e
- commit date: 2023-04-04
- overall geometric mean: 1.28x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230404-linux-x86_64-ericsnowcurrently-per_interpreter_allo-3.12.0a7+-299527e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 253 ms: 1.33x faster                                                              |
| chameleon      | 9.06 ms                                                | 6.46 ms: 1.40x faster                                                             |
| docutils       | 3.17 sec                                               | 2.56 sec: 1.24x faster                                                            |
| html5lib       | 85.9 ms                                                | 62.4 ms: 1.38x faster                                                             |
| tornado_http   | 127 ms                                                 | 91.6 ms: 1.39x faster                                                             |
| Geometric mean | (ref)                                                  | 1.35x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230404-linux-x86_64-ericsnowcurrently-per_interpreter_allo-3.12.0a7+-299527e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 87.9 ms: 1.61x faster                                                             |
| float          | 111 ms                                                 | 74.6 ms: 1.48x faster                                                             |
| pidigits       | 190 ms                                                 | 188 ms: 1.01x faster                                                              |
| Geometric mean | (ref)                                                  | 1.34x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230404-linux-x86_64-ericsnowcurrently-per_interpreter_allo-3.12.0a7+-299527e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 135 ms: 1.31x faster                                                              |
| regex_v8       | 25.0 ms                                                | 22.7 ms: 1.10x faster                                                             |
| regex_dna      | 222 ms                                                 | 204 ms: 1.09x faster                                                              |
| regex_effbot   | 3.23 ms                                                | 3.42 ms: 1.06x slower                                                             |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230404-linux-x86_64-ericsnowcurrently-per_interpreter_allo-3.12.0a7+-299527e |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 293 us: 1.56x faster                                                              |
| unpickle_pure_python | 300 us                                                 | 205 us: 1.47x faster                                                              |
| json_dumps           | 13.5 ms                                                | 9.75 ms: 1.39x faster                                                             |
| xml_etree_process    | 74.9 ms                                                | 56.6 ms: 1.32x faster                                                             |
| json_loads           | 28.8 us                                                | 24.4 us: 1.18x faster                                                             |
| xml_etree_generate   | 94.2 ms                                                | 81.7 ms: 1.15x faster                                                             |
| xml_etree_iterparse  | 111 ms                                                 | 100 ms: 1.11x faster                                                              |
| xml_etree_parse      | 163 ms                                                 | 150 ms: 1.09x faster                                                              |
| pickle_list          | 4.56 us                                                | 4.36 us: 1.04x faster                                                             |
| unpickle             | 14.1 us                                                | 13.9 us: 1.02x faster                                                             |
| pickle               | 10.3 us                                                | 10.8 us: 1.05x slower                                                             |
| unpickle_list        | 4.82 us                                                | 5.06 us: 1.05x slower                                                             |
| pickle_dict          | 27.3 us                                                | 33.3 us: 1.22x slower                                                             |
| Geometric mean       | (ref)                                                  | 1.14x faster                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230404-linux-x86_64-ericsnowcurrently-per_interpreter_allo-3.12.0a7+-299527e |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.85 ms: 1.60x faster                                                             |
| python_startup_no_site | 5.82 ms                                                | 6.53 ms: 1.12x slower                                                             |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230404-linux-x86_64-ericsnowcurrently-per_interpreter_allo-3.12.0a7+-299527e |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 10.3 ms: 1.43x faster                                                             |
| genshi_text     | 30.3 ms                                                | 21.9 ms: 1.39x faster                                                             |
| django_template | 45.9 ms                                                | 33.3 ms: 1.38x faster                                                             |
| genshi_xml      | 63.3 ms                                                | 48.9 ms: 1.29x faster                                                             |
| Geometric mean  | (ref)                                                  | 1.37x faster                                                                      |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230404-linux-x86_64-ericsnowcurrently-per_interpreter_allo-3.12.0a7+-299527e |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 29.2 ms: 2.63x faster                                                             |
| deltablue               | 7.42 ms                                                | 3.22 ms: 2.30x faster                                                             |
| asyncio_tcp             | 925 ms                                                 | 501 ms: 1.85x faster                                                              |
| logging_silent          | 175 ns                                                 | 96.3 ns: 1.82x faster                                                             |
| scimark_sor             | 197 ms                                                 | 113 ms: 1.74x faster                                                              |
| richards                | 74.9 ms                                                | 43.6 ms: 1.72x faster                                                             |
| go                      | 229 ms                                                 | 139 ms: 1.65x faster                                                              |
| raytrace                | 464 ms                                                 | 281 ms: 1.65x faster                                                              |
| nbody                   | 142 ms                                                 | 87.9 ms: 1.61x faster                                                             |
| python_startup          | 14.2 ms                                                | 8.85 ms: 1.60x faster                                                             |
| pyflate                 | 673 ms                                                 | 426 ms: 1.58x faster                                                              |
| crypto_pyaes            | 118 ms                                                 | 75.2 ms: 1.57x faster                                                             |
| scimark_monte_carlo     | 108 ms                                                 | 69.0 ms: 1.57x faster                                                             |
| pickle_pure_python      | 455 us                                                 | 293 us: 1.56x faster                                                              |
| chaos                   | 106 ms                                                 | 68.6 ms: 1.55x faster                                                             |
| hexiom                  | 9.53 ms                                                | 6.16 ms: 1.55x faster                                                             |
| scimark_lu              | 163 ms                                                 | 107 ms: 1.52x faster                                                              |
| spectral_norm           | 150 ms                                                 | 99.0 ms: 1.52x faster                                                             |
| deepcopy_memo           | 52.3 us                                                | 35.3 us: 1.48x faster                                                             |
| float                   | 111 ms                                                 | 74.6 ms: 1.48x faster                                                             |
| unpickle_pure_python    | 300 us                                                 | 205 us: 1.47x faster                                                              |
| unpack_sequence         | 64.7 ns                                                | 45.1 ns: 1.44x faster                                                             |
| mako                    | 14.8 ms                                                | 10.3 ms: 1.43x faster                                                             |
| sqlglot_parse           | 2.06 ms                                                | 1.46 ms: 1.41x faster                                                             |
| pprint_pformat          | 1.99 sec                                               | 1.41 sec: 1.40x faster                                                            |
| chameleon               | 9.06 ms                                                | 6.46 ms: 1.40x faster                                                             |
| logging_simple          | 8.07 us                                                | 5.75 us: 1.40x faster                                                             |
| logging_format          | 8.91 us                                                | 6.37 us: 1.40x faster                                                             |
| tornado_http            | 127 ms                                                 | 91.6 ms: 1.39x faster                                                             |
| sqlglot_transpile       | 2.45 ms                                                | 1.76 ms: 1.39x faster                                                             |
| genshi_text             | 30.3 ms                                                | 21.9 ms: 1.39x faster                                                             |
| json_dumps              | 13.5 ms                                                | 9.75 ms: 1.39x faster                                                             |
| pprint_safe_repr        | 955 ms                                                 | 692 ms: 1.38x faster                                                              |
| django_template         | 45.9 ms                                                | 33.3 ms: 1.38x faster                                                             |
| html5lib                | 85.9 ms                                                | 62.4 ms: 1.38x faster                                                             |
| async_tree_io           | 1.77 sec                                               | 1.30 sec: 1.37x faster                                                            |
| aiohttp                 | 1.38 ms                                                | 1.01 ms: 1.36x faster                                                             |
| async_tree_none         | 717 ms                                                 | 526 ms: 1.36x faster                                                              |
| coroutines              | 31.8 ms                                                | 23.3 ms: 1.36x faster                                                             |
| pycparser               | 1.50 sec                                               | 1.11 sec: 1.35x faster                                                            |
| gunicorn                | 1.46 ms                                                | 1.09 ms: 1.33x faster                                                             |
| 2to3                    | 336 ms                                                 | 253 ms: 1.33x faster                                                              |
| scimark_fft             | 424 ms                                                 | 319 ms: 1.33x faster                                                              |
| deepcopy                | 442 us                                                 | 333 us: 1.33x faster                                                              |
| thrift                  | 1.03 ms                                                | 780 us: 1.33x faster                                                              |
| xml_etree_process       | 74.9 ms                                                | 56.6 ms: 1.32x faster                                                             |
| async_tree_memoization  | 854 ms                                                 | 646 ms: 1.32x faster                                                              |
| regex_compile           | 177 ms                                                 | 135 ms: 1.31x faster                                                              |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.19 ms: 1.30x faster                                                             |
| genshi_xml              | 63.3 ms                                                | 48.9 ms: 1.29x faster                                                             |
| deepcopy_reduce         | 3.82 us                                                | 3.00 us: 1.27x faster                                                             |
| mypy2                   | 428 ms                                                 | 336 ms: 1.27x faster                                                              |
| async_tree_cpu_io_mixed | 951 ms                                                 | 747 ms: 1.27x faster                                                              |
| sqlglot_normalize       | 135 ms                                                 | 106 ms: 1.27x faster                                                              |
| sqlglot_optimize        | 65.3 ms                                                | 51.7 ms: 1.26x faster                                                             |
| fannkuch                | 486 ms                                                 | 389 ms: 1.25x faster                                                              |
| docutils                | 3.17 sec                                               | 2.56 sec: 1.24x faster                                                            |
| nqueens                 | 100 ms                                                 | 81.7 ms: 1.22x faster                                                             |
| sqlalchemy_declarative  | 165 ms                                                 | 137 ms: 1.20x faster                                                              |
| bench_thread_pool       | 947 us                                                 | 797 us: 1.19x faster                                                              |
| dulwich_log             | 75.9 ms                                                | 63.9 ms: 1.19x faster                                                             |
| sqlalchemy_imperative   | 21.2 ms                                                | 17.9 ms: 1.18x faster                                                             |
| json_loads              | 28.8 us                                                | 24.4 us: 1.18x faster                                                             |
| sympy_integrate         | 24.3 ms                                                | 20.7 ms: 1.17x faster                                                             |
| sympy_expand            | 545 ms                                                 | 466 ms: 1.17x faster                                                              |
| json                    | 5.42 ms                                                | 4.68 ms: 1.16x faster                                                             |
| xml_etree_generate      | 94.2 ms                                                | 81.7 ms: 1.15x faster                                                             |
| sympy_str               | 328 ms                                                 | 286 ms: 1.15x faster                                                              |
| create_gc_cycles        | 1.67 ms                                                | 1.48 ms: 1.13x faster                                                             |
| djangocms               | 35.9 us                                                | 32.2 us: 1.11x faster                                                             |
| sqlite_synth            | 2.93 us                                                | 2.64 us: 1.11x faster                                                             |
| meteor_contest          | 115 ms                                                 | 103 ms: 1.11x faster                                                              |
| xml_etree_iterparse     | 111 ms                                                 | 100 ms: 1.11x faster                                                              |
| comprehensions          | 26.8 us                                                | 24.1 us: 1.11x faster                                                             |
| sympy_sum               | 185 ms                                                 | 167 ms: 1.10x faster                                                              |
| mdp                     | 2.82 sec                                               | 2.56 sec: 1.10x faster                                                            |
| regex_v8                | 25.0 ms                                                | 22.7 ms: 1.10x faster                                                             |
| regex_dna               | 222 ms                                                 | 204 ms: 1.09x faster                                                              |
| xml_etree_parse         | 163 ms                                                 | 150 ms: 1.09x faster                                                              |
| pathlib                 | 20.0 ms                                                | 18.5 ms: 1.08x faster                                                             |
| pickle_list             | 4.56 us                                                | 4.36 us: 1.04x faster                                                             |
| unpickle                | 14.1 us                                                | 13.9 us: 1.02x faster                                                             |
| pidigits                | 190 ms                                                 | 188 ms: 1.01x faster                                                              |
| telco                   | 6.54 ms                                                | 6.60 ms: 1.01x slower                                                             |
| pickle                  | 10.3 us                                                | 10.8 us: 1.05x slower                                                             |
| unpickle_list           | 4.82 us                                                | 5.06 us: 1.05x slower                                                             |
| regex_effbot            | 3.23 ms                                                | 3.42 ms: 1.06x slower                                                             |
| gc_traversal            | 3.84 ms                                                | 4.31 ms: 1.12x slower                                                             |
| python_startup_no_site  | 5.82 ms                                                | 6.53 ms: 1.12x slower                                                             |
| dask                    | 423 ms                                                 | 515 ms: 1.22x slower                                                              |
| pickle_dict             | 27.3 us                                                | 33.3 us: 1.22x slower                                                             |
| coverage                | 72.8 ms                                                | 98.3 ms: 1.35x slower                                                             |
| Geometric mean          | (ref)                                                  | 1.28x faster                                                                      |

Benchmark hidden because not significant (2): async_generators, bench_mp_pool
Ignored benchmarks (6) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.23x
