
# Results vs. 3.10.4

- fork: ericsnowcurrently
- ref: per_interpreter_gil_
- machine: linux-x86_64
- commit hash: d43bb5f
- commit date: 2023-04-10
- overall geometric mean: 1.30x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230410-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-d43bb5f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 252 ms: 1.33x faster                                                              |
| chameleon      | 9.06 ms                                                | 6.52 ms: 1.39x faster                                                             |
| docutils       | 3.17 sec                                               | 2.57 sec: 1.23x faster                                                            |
| html5lib       | 85.9 ms                                                | 62.4 ms: 1.38x faster                                                             |
| tornado_http   | 127 ms                                                 | 94.1 ms: 1.35x faster                                                             |
| Geometric mean | (ref)                                                  | 1.34x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230410-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-d43bb5f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 84.4 ms: 1.68x faster                                                             |
| float          | 111 ms                                                 | 74.3 ms: 1.49x faster                                                             |
| pidigits       | 190 ms                                                 | 197 ms: 1.04x slower                                                              |
| Geometric mean | (ref)                                                  | 1.34x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230410-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-d43bb5f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 133 ms: 1.33x faster                                                              |
| regex_v8       | 25.0 ms                                                | 22.5 ms: 1.12x faster                                                             |
| regex_dna      | 222 ms                                                 | 208 ms: 1.07x faster                                                              |
| regex_effbot   | 3.23 ms                                                | 3.64 ms: 1.13x slower                                                             |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230410-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-d43bb5f |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 289 us: 1.58x faster                                                              |
| unpickle_pure_python | 300 us                                                 | 201 us: 1.49x faster                                                              |
| json_dumps           | 13.5 ms                                                | 9.80 ms: 1.38x faster                                                             |
| xml_etree_process    | 74.9 ms                                                | 55.5 ms: 1.35x faster                                                             |
| json_loads           | 28.8 us                                                | 24.4 us: 1.18x faster                                                             |
| xml_etree_generate   | 94.2 ms                                                | 81.2 ms: 1.16x faster                                                             |
| xml_etree_iterparse  | 111 ms                                                 | 99.7 ms: 1.12x faster                                                             |
| xml_etree_parse      | 163 ms                                                 | 151 ms: 1.08x faster                                                              |
| pickle_list          | 4.56 us                                                | 4.35 us: 1.05x faster                                                             |
| unpickle             | 14.1 us                                                | 13.7 us: 1.03x faster                                                             |
| unpickle_list        | 4.82 us                                                | 4.91 us: 1.02x slower                                                             |
| pickle               | 10.3 us                                                | 10.7 us: 1.04x slower                                                             |
| pickle_dict          | 27.3 us                                                | 31.9 us: 1.17x slower                                                             |
| Geometric mean       | (ref)                                                  | 1.15x faster                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230410-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-d43bb5f |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.92 ms: 1.59x faster                                                             |
| python_startup_no_site | 5.82 ms                                                | 6.59 ms: 1.13x slower                                                             |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230410-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-d43bb5f |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 10.2 ms: 1.44x faster                                                             |
| genshi_text     | 30.3 ms                                                | 21.7 ms: 1.40x faster                                                             |
| django_template | 45.9 ms                                                | 33.0 ms: 1.39x faster                                                             |
| genshi_xml      | 63.3 ms                                                | 48.6 ms: 1.30x faster                                                             |
| Geometric mean  | (ref)                                                  | 1.38x faster                                                                      |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230410-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-d43bb5f |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 30.1 ms: 2.55x faster                                                             |
| deltablue               | 7.42 ms                                                | 3.23 ms: 2.30x faster                                                             |
| asyncio_tcp             | 925 ms                                                 | 503 ms: 1.84x faster                                                              |
| logging_silent          | 175 ns                                                 | 97.4 ns: 1.80x faster                                                             |
| scimark_sor             | 197 ms                                                 | 112 ms: 1.75x faster                                                              |
| richards                | 74.9 ms                                                | 43.1 ms: 1.74x faster                                                             |
| sqlglot_parse           | 2.06 ms                                                | 1.23 ms: 1.68x faster                                                             |
| nbody                   | 142 ms                                                 | 84.4 ms: 1.68x faster                                                             |
| go                      | 229 ms                                                 | 137 ms: 1.67x faster                                                              |
| raytrace                | 464 ms                                                 | 279 ms: 1.66x faster                                                              |
| scimark_monte_carlo     | 108 ms                                                 | 66.4 ms: 1.63x faster                                                             |
| sqlglot_transpile       | 2.45 ms                                                | 1.51 ms: 1.63x faster                                                             |
| chaos                   | 106 ms                                                 | 65.4 ms: 1.63x faster                                                             |
| pyflate                 | 673 ms                                                 | 422 ms: 1.59x faster                                                              |
| python_startup          | 14.2 ms                                                | 8.92 ms: 1.59x faster                                                             |
| crypto_pyaes            | 118 ms                                                 | 75.0 ms: 1.58x faster                                                             |
| hexiom                  | 9.53 ms                                                | 6.04 ms: 1.58x faster                                                             |
| pickle_pure_python      | 455 us                                                 | 289 us: 1.58x faster                                                              |
| spectral_norm           | 150 ms                                                 | 97.8 ms: 1.53x faster                                                             |
| scimark_lu              | 163 ms                                                 | 107 ms: 1.53x faster                                                              |
| deepcopy_memo           | 52.3 us                                                | 34.5 us: 1.52x faster                                                             |
| unpickle_pure_python    | 300 us                                                 | 201 us: 1.49x faster                                                              |
| float                   | 111 ms                                                 | 74.3 ms: 1.49x faster                                                             |
| unpack_sequence         | 64.7 ns                                                | 43.8 ns: 1.48x faster                                                             |
| mako                    | 14.8 ms                                                | 10.2 ms: 1.44x faster                                                             |
| coroutines              | 31.8 ms                                                | 22.4 ms: 1.42x faster                                                             |
| logging_simple          | 8.07 us                                                | 5.75 us: 1.40x faster                                                             |
| logging_format          | 8.91 us                                                | 6.36 us: 1.40x faster                                                             |
| genshi_text             | 30.3 ms                                                | 21.7 ms: 1.40x faster                                                             |
| pprint_pformat          | 1.99 sec                                               | 1.43 sec: 1.39x faster                                                            |
| django_template         | 45.9 ms                                                | 33.0 ms: 1.39x faster                                                             |
| async_tree_none         | 717 ms                                                 | 516 ms: 1.39x faster                                                              |
| chameleon               | 9.06 ms                                                | 6.52 ms: 1.39x faster                                                             |
| pprint_safe_repr        | 955 ms                                                 | 690 ms: 1.38x faster                                                              |
| json_dumps              | 13.5 ms                                                | 9.80 ms: 1.38x faster                                                             |
| html5lib                | 85.9 ms                                                | 62.4 ms: 1.38x faster                                                             |
| async_tree_memoization  | 854 ms                                                 | 620 ms: 1.38x faster                                                              |
| scimark_fft             | 424 ms                                                 | 308 ms: 1.38x faster                                                              |
| async_tree_io           | 1.77 sec                                               | 1.29 sec: 1.37x faster                                                            |
| aiohttp                 | 1.38 ms                                                | 1.01 ms: 1.37x faster                                                             |
| tornado_http            | 127 ms                                                 | 94.1 ms: 1.35x faster                                                             |
| xml_etree_process       | 74.9 ms                                                | 55.5 ms: 1.35x faster                                                             |
| thrift                  | 1.03 ms                                                | 771 us: 1.34x faster                                                              |
| 2to3                    | 336 ms                                                 | 252 ms: 1.33x faster                                                              |
| regex_compile           | 177 ms                                                 | 133 ms: 1.33x faster                                                              |
| gunicorn                | 1.46 ms                                                | 1.10 ms: 1.33x faster                                                             |
| deepcopy                | 442 us                                                 | 334 us: 1.32x faster                                                              |
| genshi_xml              | 63.3 ms                                                | 48.6 ms: 1.30x faster                                                             |
| async_tree_cpu_io_mixed | 951 ms                                                 | 732 ms: 1.30x faster                                                              |
| sqlglot_normalize       | 135 ms                                                 | 104 ms: 1.30x faster                                                              |
| pycparser               | 1.50 sec                                               | 1.16 sec: 1.30x faster                                                            |
| sqlglot_optimize        | 65.3 ms                                                | 51.1 ms: 1.28x faster                                                             |
| mypy2                   | 428 ms                                                 | 336 ms: 1.28x faster                                                              |
| deepcopy_reduce         | 3.82 us                                                | 3.00 us: 1.28x faster                                                             |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.29 ms: 1.27x faster                                                             |
| fannkuch                | 486 ms                                                 | 383 ms: 1.27x faster                                                              |
| docutils                | 3.17 sec                                               | 2.57 sec: 1.23x faster                                                            |
| comprehensions          | 26.8 us                                                | 21.8 us: 1.23x faster                                                             |
| nqueens                 | 100 ms                                                 | 82.1 ms: 1.22x faster                                                             |
| sqlalchemy_declarative  | 165 ms                                                 | 137 ms: 1.21x faster                                                              |
| dulwich_log             | 75.9 ms                                                | 63.7 ms: 1.19x faster                                                             |
| bench_thread_pool       | 947 us                                                 | 796 us: 1.19x faster                                                              |
| sympy_integrate         | 24.3 ms                                                | 20.5 ms: 1.18x faster                                                             |
| sqlalchemy_imperative   | 21.2 ms                                                | 17.9 ms: 1.18x faster                                                             |
| json_loads              | 28.8 us                                                | 24.4 us: 1.18x faster                                                             |
| sympy_expand            | 545 ms                                                 | 462 ms: 1.18x faster                                                              |
| xml_etree_generate      | 94.2 ms                                                | 81.2 ms: 1.16x faster                                                             |
| sympy_str               | 328 ms                                                 | 284 ms: 1.16x faster                                                              |
| json                    | 5.42 ms                                                | 4.70 ms: 1.15x faster                                                             |
| meteor_contest          | 115 ms                                                 | 102 ms: 1.12x faster                                                              |
| xml_etree_iterparse     | 111 ms                                                 | 99.7 ms: 1.12x faster                                                             |
| regex_v8                | 25.0 ms                                                | 22.5 ms: 1.12x faster                                                             |
| sqlite_synth            | 2.93 us                                                | 2.64 us: 1.11x faster                                                             |
| create_gc_cycles        | 1.67 ms                                                | 1.50 ms: 1.11x faster                                                             |
| sympy_sum               | 185 ms                                                 | 166 ms: 1.11x faster                                                              |
| djangocms               | 35.9 us                                                | 32.4 us: 1.11x faster                                                             |
| pathlib                 | 20.0 ms                                                | 18.3 ms: 1.09x faster                                                             |
| mdp                     | 2.82 sec                                               | 2.61 sec: 1.08x faster                                                            |
| xml_etree_parse         | 163 ms                                                 | 151 ms: 1.08x faster                                                              |
| regex_dna               | 222 ms                                                 | 208 ms: 1.07x faster                                                              |
| pickle_list             | 4.56 us                                                | 4.35 us: 1.05x faster                                                             |
| unpickle                | 14.1 us                                                | 13.7 us: 1.03x faster                                                             |
| async_generators        | 425 ms                                                 | 412 ms: 1.03x faster                                                              |
| telco                   | 6.54 ms                                                | 6.42 ms: 1.02x faster                                                             |
| gc_traversal            | 3.84 ms                                                | 3.85 ms: 1.00x slower                                                             |
| unpickle_list           | 4.82 us                                                | 4.91 us: 1.02x slower                                                             |
| pidigits                | 190 ms                                                 | 197 ms: 1.04x slower                                                              |
| pickle                  | 10.3 us                                                | 10.7 us: 1.04x slower                                                             |
| regex_effbot            | 3.23 ms                                                | 3.64 ms: 1.13x slower                                                             |
| python_startup_no_site  | 5.82 ms                                                | 6.59 ms: 1.13x slower                                                             |
| pickle_dict             | 27.3 us                                                | 31.9 us: 1.17x slower                                                             |
| dask                    | 423 ms                                                 | 504 ms: 1.19x slower                                                              |
| coverage                | 72.8 ms                                                | 97.4 ms: 1.34x slower                                                             |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                                      |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (6) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.24x
