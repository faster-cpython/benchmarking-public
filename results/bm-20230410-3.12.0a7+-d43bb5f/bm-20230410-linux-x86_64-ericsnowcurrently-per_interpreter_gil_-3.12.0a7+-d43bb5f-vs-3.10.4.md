
# Results vs. 3.10.4

- fork: ericsnowcurrently
- ref: per_interpreter_gil_
- machine: linux-x86_64
- commit hash: d43bb5f
- commit date: 2023-04-10
- overall geometric mean: 1.30x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230410-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-d43bb5f |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                              | 252 ms: 1.33x faster                                                              |
| chameleon      | 9.13 ms                                                             | 6.52 ms: 1.40x faster                                                             |
| docutils       | 3.19 sec                                                            | 2.57 sec: 1.24x faster                                                            |
| html5lib       | 86.4 ms                                                             | 62.4 ms: 1.38x faster                                                             |
| tornado_http   | 129 ms                                                              | 94.1 ms: 1.37x faster                                                             |
| Geometric mean | (ref)                                                               | 1.34x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230410-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-d43bb5f |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 146 ms                                                              | 84.4 ms: 1.73x faster                                                             |
| float          | 110 ms                                                              | 74.3 ms: 1.48x faster                                                             |
| pidigits       | 190 ms                                                              | 197 ms: 1.04x slower                                                              |
| Geometric mean | (ref)                                                               | 1.35x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230410-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-d43bb5f |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                              | 133 ms: 1.33x faster                                                              |
| regex_v8       | 24.9 ms                                                             | 22.5 ms: 1.11x faster                                                             |
| regex_dna      | 213 ms                                                              | 208 ms: 1.03x faster                                                              |
| regex_effbot   | 3.22 ms                                                             | 3.64 ms: 1.13x slower                                                             |
| Geometric mean | (ref)                                                               | 1.08x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230410-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-d43bb5f |
|----------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pickle_pure_python   | 457 us                                                              | 289 us: 1.58x faster                                                              |
| unpickle_pure_python | 300 us                                                              | 201 us: 1.49x faster                                                              |
| json_dumps           | 13.7 ms                                                             | 9.80 ms: 1.40x faster                                                             |
| xml_etree_process    | 74.8 ms                                                             | 55.5 ms: 1.35x faster                                                             |
| json_loads           | 29.3 us                                                             | 24.4 us: 1.20x faster                                                             |
| xml_etree_generate   | 94.9 ms                                                             | 81.2 ms: 1.17x faster                                                             |
| xml_etree_iterparse  | 111 ms                                                              | 99.7 ms: 1.12x faster                                                             |
| unpickle             | 15.0 us                                                             | 13.7 us: 1.09x faster                                                             |
| pickle_list          | 4.73 us                                                             | 4.35 us: 1.09x faster                                                             |
| xml_etree_parse      | 164 ms                                                              | 151 ms: 1.08x faster                                                              |
| unpickle_list        | 4.94 us                                                             | 4.91 us: 1.01x faster                                                             |
| pickle               | 10.2 us                                                             | 10.7 us: 1.05x slower                                                             |
| pickle_dict          | 27.8 us                                                             | 31.9 us: 1.15x slower                                                             |
| Geometric mean       | (ref)                                                               | 1.17x faster                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230410-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-d43bb5f |
|------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                             | 8.92 ms: 1.59x faster                                                             |
| python_startup_no_site | 5.80 ms                                                             | 6.59 ms: 1.14x slower                                                             |
| Geometric mean         | (ref)                                                               | 1.18x faster                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230410-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-d43bb5f |
|-----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                             | 10.2 ms: 1.44x faster                                                             |
| genshi_text     | 30.4 ms                                                             | 21.7 ms: 1.40x faster                                                             |
| django_template | 45.8 ms                                                             | 33.0 ms: 1.39x faster                                                             |
| genshi_xml      | 64.3 ms                                                             | 48.6 ms: 1.32x faster                                                             |
| Geometric mean  | (ref)                                                               | 1.39x faster                                                                      |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230410-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-d43bb5f |
|-------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| generators              | 75.7 ms                                                             | 30.1 ms: 2.51x faster                                                             |
| deltablue               | 7.30 ms                                                             | 3.23 ms: 2.26x faster                                                             |
| asyncio_tcp             | 922 ms                                                              | 503 ms: 1.83x faster                                                              |
| scimark_sor             | 198 ms                                                              | 112 ms: 1.76x faster                                                              |
| logging_silent          | 169 ns                                                              | 97.4 ns: 1.73x faster                                                             |
| nbody                   | 146 ms                                                              | 84.4 ms: 1.73x faster                                                             |
| richards                | 74.2 ms                                                             | 43.1 ms: 1.72x faster                                                             |
| sqlglot_parse           | 2.07 ms                                                             | 1.23 ms: 1.69x faster                                                             |
| raytrace                | 470 ms                                                              | 279 ms: 1.68x faster                                                              |
| go                      | 226 ms                                                              | 137 ms: 1.65x faster                                                              |
| scimark_monte_carlo     | 109 ms                                                              | 66.4 ms: 1.63x faster                                                             |
| sqlglot_transpile       | 2.45 ms                                                             | 1.51 ms: 1.63x faster                                                             |
| chaos                   | 106 ms                                                              | 65.4 ms: 1.62x faster                                                             |
| pyflate                 | 671 ms                                                              | 422 ms: 1.59x faster                                                              |
| python_startup          | 14.1 ms                                                             | 8.92 ms: 1.59x faster                                                             |
| pickle_pure_python      | 457 us                                                              | 289 us: 1.58x faster                                                              |
| hexiom                  | 9.50 ms                                                             | 6.04 ms: 1.57x faster                                                             |
| crypto_pyaes            | 117 ms                                                              | 75.0 ms: 1.55x faster                                                             |
| spectral_norm           | 150 ms                                                              | 97.8 ms: 1.54x faster                                                             |
| deepcopy_memo           | 51.8 us                                                             | 34.5 us: 1.50x faster                                                             |
| scimark_lu              | 160 ms                                                              | 107 ms: 1.50x faster                                                              |
| unpack_sequence         | 65.6 ns                                                             | 43.8 ns: 1.50x faster                                                             |
| unpickle_pure_python    | 300 us                                                              | 201 us: 1.49x faster                                                              |
| float                   | 110 ms                                                              | 74.3 ms: 1.48x faster                                                             |
| mako                    | 14.7 ms                                                             | 10.2 ms: 1.44x faster                                                             |
| logging_simple          | 8.21 us                                                             | 5.75 us: 1.43x faster                                                             |
| logging_format          | 9.07 us                                                             | 6.36 us: 1.43x faster                                                             |
| coroutines              | 31.8 ms                                                             | 22.4 ms: 1.42x faster                                                             |
| genshi_text             | 30.4 ms                                                             | 21.7 ms: 1.40x faster                                                             |
| chameleon               | 9.13 ms                                                             | 6.52 ms: 1.40x faster                                                             |
| json_dumps              | 13.7 ms                                                             | 9.80 ms: 1.40x faster                                                             |
| django_template         | 45.8 ms                                                             | 33.0 ms: 1.39x faster                                                             |
| pprint_pformat          | 1.98 sec                                                            | 1.43 sec: 1.39x faster                                                            |
| html5lib                | 86.4 ms                                                             | 62.4 ms: 1.38x faster                                                             |
| scimark_fft             | 425 ms                                                              | 308 ms: 1.38x faster                                                              |
| pprint_safe_repr        | 953 ms                                                              | 690 ms: 1.38x faster                                                              |
| async_tree_none         | 713 ms                                                              | 516 ms: 1.38x faster                                                              |
| async_tree_io           | 1.78 sec                                                            | 1.29 sec: 1.38x faster                                                            |
| async_tree_memoization  | 853 ms                                                              | 620 ms: 1.37x faster                                                              |
| tornado_http            | 129 ms                                                              | 94.1 ms: 1.37x faster                                                             |
| xml_etree_process       | 74.8 ms                                                             | 55.5 ms: 1.35x faster                                                             |
| thrift                  | 1.04 ms                                                             | 771 us: 1.35x faster                                                              |
| aiohttp                 | 1.35 ms                                                             | 1.01 ms: 1.34x faster                                                             |
| regex_compile           | 177 ms                                                              | 133 ms: 1.33x faster                                                              |
| 2to3                    | 336 ms                                                              | 252 ms: 1.33x faster                                                              |
| pycparser               | 1.53 sec                                                            | 1.16 sec: 1.32x faster                                                            |
| genshi_xml              | 64.3 ms                                                             | 48.6 ms: 1.32x faster                                                             |
| deepcopy                | 438 us                                                              | 334 us: 1.31x faster                                                              |
| scimark_sparse_mat_mult | 5.62 ms                                                             | 4.29 ms: 1.31x faster                                                             |
| gunicorn                | 1.43 ms                                                             | 1.10 ms: 1.31x faster                                                             |
| async_tree_cpu_io_mixed | 944 ms                                                              | 732 ms: 1.29x faster                                                              |
| sqlglot_normalize       | 135 ms                                                              | 104 ms: 1.29x faster                                                              |
| mypy2                   | 432 ms                                                              | 336 ms: 1.29x faster                                                              |
| sqlglot_optimize        | 65.3 ms                                                             | 51.1 ms: 1.28x faster                                                             |
| fannkuch                | 485 ms                                                              | 383 ms: 1.27x faster                                                              |
| deepcopy_reduce         | 3.80 us                                                             | 3.00 us: 1.27x faster                                                             |
| comprehensions          | 27.3 us                                                             | 21.8 us: 1.25x faster                                                             |
| docutils                | 3.19 sec                                                            | 2.57 sec: 1.24x faster                                                            |
| sqlalchemy_declarative  | 166 ms                                                              | 137 ms: 1.22x faster                                                              |
| nqueens                 | 98.8 ms                                                             | 82.1 ms: 1.20x faster                                                             |
| json_loads              | 29.3 us                                                             | 24.4 us: 1.20x faster                                                             |
| bench_thread_pool       | 954 us                                                              | 796 us: 1.20x faster                                                              |
| dulwich_log             | 76.3 ms                                                             | 63.7 ms: 1.20x faster                                                             |
| sympy_integrate         | 24.3 ms                                                             | 20.5 ms: 1.18x faster                                                             |
| sqlalchemy_imperative   | 21.2 ms                                                             | 17.9 ms: 1.18x faster                                                             |
| sympy_expand            | 540 ms                                                              | 462 ms: 1.17x faster                                                              |
| xml_etree_generate      | 94.9 ms                                                             | 81.2 ms: 1.17x faster                                                             |
| sympy_str               | 328 ms                                                              | 284 ms: 1.15x faster                                                              |
| json                    | 5.41 ms                                                             | 4.70 ms: 1.15x faster                                                             |
| sqlite_synth            | 2.97 us                                                             | 2.64 us: 1.13x faster                                                             |
| meteor_contest          | 115 ms                                                              | 102 ms: 1.12x faster                                                              |
| djangocms               | 36.3 us                                                             | 32.4 us: 1.12x faster                                                             |
| xml_etree_iterparse     | 111 ms                                                              | 99.7 ms: 1.12x faster                                                             |
| sympy_sum               | 185 ms                                                              | 166 ms: 1.11x faster                                                              |
| regex_v8                | 24.9 ms                                                             | 22.5 ms: 1.11x faster                                                             |
| unpickle                | 15.0 us                                                             | 13.7 us: 1.09x faster                                                             |
| create_gc_cycles        | 1.64 ms                                                             | 1.50 ms: 1.09x faster                                                             |
| pickle_list             | 4.73 us                                                             | 4.35 us: 1.09x faster                                                             |
| xml_etree_parse         | 164 ms                                                              | 151 ms: 1.08x faster                                                              |
| pathlib                 | 19.8 ms                                                             | 18.3 ms: 1.08x faster                                                             |
| mdp                     | 2.75 sec                                                            | 2.61 sec: 1.05x faster                                                            |
| telco                   | 6.67 ms                                                             | 6.42 ms: 1.04x faster                                                             |
| regex_dna               | 213 ms                                                              | 208 ms: 1.03x faster                                                              |
| async_generators        | 420 ms                                                              | 412 ms: 1.02x faster                                                              |
| unpickle_list           | 4.94 us                                                             | 4.91 us: 1.01x faster                                                             |
| pidigits                | 190 ms                                                              | 197 ms: 1.04x slower                                                              |
| pickle                  | 10.2 us                                                             | 10.7 us: 1.05x slower                                                             |
| gc_traversal            | 3.53 ms                                                             | 3.85 ms: 1.09x slower                                                             |
| regex_effbot            | 3.22 ms                                                             | 3.64 ms: 1.13x slower                                                             |
| python_startup_no_site  | 5.80 ms                                                             | 6.59 ms: 1.14x slower                                                             |
| pickle_dict             | 27.8 us                                                             | 31.9 us: 1.15x slower                                                             |
| dask                    | 437 ms                                                              | 504 ms: 1.15x slower                                                              |
| coverage                | 70.6 ms                                                             | 97.4 ms: 1.38x slower                                                             |
| Geometric mean          | (ref)                                                               | 1.30x faster                                                                      |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120.json: flaskblogging, pylint
