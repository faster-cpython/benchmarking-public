
# Results vs. 3.10.4

- fork: ericsnowcurrently
- ref: per_interpreter_allo
- machine: linux-x86_64
- commit hash: 299527e
- commit date: 2023-04-04
- overall geometric mean: 1.28x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230404-linux-x86_64-ericsnowcurrently-per_interpreter_allo-3.12.0a7+-299527e |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                              | 253 ms: 1.33x faster                                                              |
| chameleon      | 9.13 ms                                                             | 6.46 ms: 1.41x faster                                                             |
| docutils       | 3.19 sec                                                            | 2.56 sec: 1.25x faster                                                            |
| html5lib       | 86.4 ms                                                             | 62.4 ms: 1.38x faster                                                             |
| tornado_http   | 129 ms                                                              | 91.6 ms: 1.41x faster                                                             |
| Geometric mean | (ref)                                                               | 1.35x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230404-linux-x86_64-ericsnowcurrently-per_interpreter_allo-3.12.0a7+-299527e |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 146 ms                                                              | 87.9 ms: 1.66x faster                                                             |
| float          | 110 ms                                                              | 74.6 ms: 1.47x faster                                                             |
| pidigits       | 190 ms                                                              | 188 ms: 1.01x faster                                                              |
| Geometric mean | (ref)                                                               | 1.35x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230404-linux-x86_64-ericsnowcurrently-per_interpreter_allo-3.12.0a7+-299527e |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                              | 135 ms: 1.31x faster                                                              |
| regex_v8       | 24.9 ms                                                             | 22.7 ms: 1.10x faster                                                             |
| regex_dna      | 213 ms                                                              | 204 ms: 1.05x faster                                                              |
| regex_effbot   | 3.22 ms                                                             | 3.42 ms: 1.06x slower                                                             |
| Geometric mean | (ref)                                                               | 1.09x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230404-linux-x86_64-ericsnowcurrently-per_interpreter_allo-3.12.0a7+-299527e |
|----------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pickle_pure_python   | 457 us                                                              | 293 us: 1.56x faster                                                              |
| unpickle_pure_python | 300 us                                                              | 205 us: 1.46x faster                                                              |
| json_dumps           | 13.7 ms                                                             | 9.75 ms: 1.40x faster                                                             |
| xml_etree_process    | 74.8 ms                                                             | 56.6 ms: 1.32x faster                                                             |
| json_loads           | 29.3 us                                                             | 24.4 us: 1.20x faster                                                             |
| xml_etree_generate   | 94.9 ms                                                             | 81.7 ms: 1.16x faster                                                             |
| xml_etree_iterparse  | 111 ms                                                              | 100 ms: 1.11x faster                                                              |
| xml_etree_parse      | 164 ms                                                              | 150 ms: 1.09x faster                                                              |
| pickle_list          | 4.73 us                                                             | 4.36 us: 1.08x faster                                                             |
| unpickle             | 15.0 us                                                             | 13.9 us: 1.08x faster                                                             |
| unpickle_list        | 4.94 us                                                             | 5.06 us: 1.02x slower                                                             |
| pickle               | 10.2 us                                                             | 10.8 us: 1.06x slower                                                             |
| pickle_dict          | 27.8 us                                                             | 33.3 us: 1.20x slower                                                             |
| Geometric mean       | (ref)                                                               | 1.15x faster                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230404-linux-x86_64-ericsnowcurrently-per_interpreter_allo-3.12.0a7+-299527e |
|------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                             | 8.85 ms: 1.60x faster                                                             |
| python_startup_no_site | 5.80 ms                                                             | 6.53 ms: 1.13x slower                                                             |
| Geometric mean         | (ref)                                                               | 1.19x faster                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230404-linux-x86_64-ericsnowcurrently-per_interpreter_allo-3.12.0a7+-299527e |
|-----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                             | 10.3 ms: 1.43x faster                                                             |
| genshi_text     | 30.4 ms                                                             | 21.9 ms: 1.39x faster                                                             |
| django_template | 45.8 ms                                                             | 33.3 ms: 1.38x faster                                                             |
| genshi_xml      | 64.3 ms                                                             | 48.9 ms: 1.31x faster                                                             |
| Geometric mean  | (ref)                                                               | 1.38x faster                                                                      |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230404-linux-x86_64-ericsnowcurrently-per_interpreter_allo-3.12.0a7+-299527e |
|-------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| generators              | 75.7 ms                                                             | 29.2 ms: 2.59x faster                                                             |
| deltablue               | 7.30 ms                                                             | 3.22 ms: 2.26x faster                                                             |
| asyncio_tcp             | 922 ms                                                              | 501 ms: 1.84x faster                                                              |
| logging_silent          | 169 ns                                                              | 96.3 ns: 1.75x faster                                                             |
| scimark_sor             | 198 ms                                                              | 113 ms: 1.75x faster                                                              |
| richards                | 74.2 ms                                                             | 43.6 ms: 1.70x faster                                                             |
| raytrace                | 470 ms                                                              | 281 ms: 1.67x faster                                                              |
| nbody                   | 146 ms                                                              | 87.9 ms: 1.66x faster                                                             |
| go                      | 226 ms                                                              | 139 ms: 1.63x faster                                                              |
| python_startup          | 14.1 ms                                                             | 8.85 ms: 1.60x faster                                                             |
| pyflate                 | 671 ms                                                              | 426 ms: 1.57x faster                                                              |
| scimark_monte_carlo     | 109 ms                                                              | 69.0 ms: 1.57x faster                                                             |
| pickle_pure_python      | 457 us                                                              | 293 us: 1.56x faster                                                              |
| crypto_pyaes            | 117 ms                                                              | 75.2 ms: 1.55x faster                                                             |
| chaos                   | 106 ms                                                              | 68.6 ms: 1.54x faster                                                             |
| hexiom                  | 9.50 ms                                                             | 6.16 ms: 1.54x faster                                                             |
| spectral_norm           | 150 ms                                                              | 99.0 ms: 1.52x faster                                                             |
| scimark_lu              | 160 ms                                                              | 107 ms: 1.49x faster                                                              |
| float                   | 110 ms                                                              | 74.6 ms: 1.47x faster                                                             |
| deepcopy_memo           | 51.8 us                                                             | 35.3 us: 1.47x faster                                                             |
| unpickle_pure_python    | 300 us                                                              | 205 us: 1.46x faster                                                              |
| unpack_sequence         | 65.6 ns                                                             | 45.1 ns: 1.46x faster                                                             |
| mako                    | 14.7 ms                                                             | 10.3 ms: 1.43x faster                                                             |
| logging_simple          | 8.21 us                                                             | 5.75 us: 1.43x faster                                                             |
| logging_format          | 9.07 us                                                             | 6.37 us: 1.42x faster                                                             |
| sqlglot_parse           | 2.07 ms                                                             | 1.46 ms: 1.42x faster                                                             |
| chameleon               | 9.13 ms                                                             | 6.46 ms: 1.41x faster                                                             |
| tornado_http            | 129 ms                                                              | 91.6 ms: 1.41x faster                                                             |
| json_dumps              | 13.7 ms                                                             | 9.75 ms: 1.40x faster                                                             |
| pprint_pformat          | 1.98 sec                                                            | 1.41 sec: 1.40x faster                                                            |
| sqlglot_transpile       | 2.45 ms                                                             | 1.76 ms: 1.39x faster                                                             |
| genshi_text             | 30.4 ms                                                             | 21.9 ms: 1.39x faster                                                             |
| html5lib                | 86.4 ms                                                             | 62.4 ms: 1.38x faster                                                             |
| pprint_safe_repr        | 953 ms                                                              | 692 ms: 1.38x faster                                                              |
| django_template         | 45.8 ms                                                             | 33.3 ms: 1.38x faster                                                             |
| pycparser               | 1.53 sec                                                            | 1.11 sec: 1.37x faster                                                            |
| async_tree_io           | 1.78 sec                                                            | 1.30 sec: 1.37x faster                                                            |
| coroutines              | 31.8 ms                                                             | 23.3 ms: 1.36x faster                                                             |
| async_tree_none         | 713 ms                                                              | 526 ms: 1.36x faster                                                              |
| scimark_sparse_mat_mult | 5.62 ms                                                             | 4.19 ms: 1.34x faster                                                             |
| scimark_fft             | 425 ms                                                              | 319 ms: 1.33x faster                                                              |
| aiohttp                 | 1.35 ms                                                             | 1.01 ms: 1.33x faster                                                             |
| thrift                  | 1.04 ms                                                             | 780 us: 1.33x faster                                                              |
| 2to3                    | 336 ms                                                              | 253 ms: 1.33x faster                                                              |
| xml_etree_process       | 74.8 ms                                                             | 56.6 ms: 1.32x faster                                                             |
| async_tree_memoization  | 853 ms                                                              | 646 ms: 1.32x faster                                                              |
| genshi_xml              | 64.3 ms                                                             | 48.9 ms: 1.31x faster                                                             |
| deepcopy                | 438 us                                                              | 333 us: 1.31x faster                                                              |
| gunicorn                | 1.43 ms                                                             | 1.09 ms: 1.31x faster                                                             |
| regex_compile           | 177 ms                                                              | 135 ms: 1.31x faster                                                              |
| mypy2                   | 432 ms                                                              | 336 ms: 1.28x faster                                                              |
| deepcopy_reduce         | 3.80 us                                                             | 3.00 us: 1.27x faster                                                             |
| async_tree_cpu_io_mixed | 944 ms                                                              | 747 ms: 1.26x faster                                                              |
| sqlglot_normalize       | 135 ms                                                              | 106 ms: 1.26x faster                                                              |
| sqlglot_optimize        | 65.3 ms                                                             | 51.7 ms: 1.26x faster                                                             |
| docutils                | 3.19 sec                                                            | 2.56 sec: 1.25x faster                                                            |
| fannkuch                | 485 ms                                                              | 389 ms: 1.25x faster                                                              |
| nqueens                 | 98.8 ms                                                             | 81.7 ms: 1.21x faster                                                             |
| sqlalchemy_declarative  | 166 ms                                                              | 137 ms: 1.21x faster                                                              |
| json_loads              | 29.3 us                                                             | 24.4 us: 1.20x faster                                                             |
| bench_thread_pool       | 954 us                                                              | 797 us: 1.20x faster                                                              |
| dulwich_log             | 76.3 ms                                                             | 63.9 ms: 1.19x faster                                                             |
| sqlalchemy_imperative   | 21.2 ms                                                             | 17.9 ms: 1.18x faster                                                             |
| sympy_integrate         | 24.3 ms                                                             | 20.7 ms: 1.17x faster                                                             |
| xml_etree_generate      | 94.9 ms                                                             | 81.7 ms: 1.16x faster                                                             |
| sympy_expand            | 540 ms                                                              | 466 ms: 1.16x faster                                                              |
| json                    | 5.41 ms                                                             | 4.68 ms: 1.16x faster                                                             |
| sympy_str               | 328 ms                                                              | 286 ms: 1.15x faster                                                              |
| comprehensions          | 27.3 us                                                             | 24.1 us: 1.13x faster                                                             |
| sqlite_synth            | 2.97 us                                                             | 2.64 us: 1.13x faster                                                             |
| djangocms               | 36.3 us                                                             | 32.2 us: 1.13x faster                                                             |
| meteor_contest          | 115 ms                                                              | 103 ms: 1.11x faster                                                              |
| xml_etree_iterparse     | 111 ms                                                              | 100 ms: 1.11x faster                                                              |
| create_gc_cycles        | 1.64 ms                                                             | 1.48 ms: 1.11x faster                                                             |
| sympy_sum               | 185 ms                                                              | 167 ms: 1.11x faster                                                              |
| regex_v8                | 24.9 ms                                                             | 22.7 ms: 1.10x faster                                                             |
| xml_etree_parse         | 164 ms                                                              | 150 ms: 1.09x faster                                                              |
| pickle_list             | 4.73 us                                                             | 4.36 us: 1.08x faster                                                             |
| unpickle                | 15.0 us                                                             | 13.9 us: 1.08x faster                                                             |
| mdp                     | 2.75 sec                                                            | 2.56 sec: 1.08x faster                                                            |
| pathlib                 | 19.8 ms                                                             | 18.5 ms: 1.07x faster                                                             |
| regex_dna               | 213 ms                                                              | 204 ms: 1.05x faster                                                              |
| telco                   | 6.67 ms                                                             | 6.60 ms: 1.01x faster                                                             |
| pidigits                | 190 ms                                                              | 188 ms: 1.01x faster                                                              |
| async_generators        | 420 ms                                                              | 425 ms: 1.01x slower                                                              |
| unpickle_list           | 4.94 us                                                             | 5.06 us: 1.02x slower                                                             |
| pickle                  | 10.2 us                                                             | 10.8 us: 1.06x slower                                                             |
| regex_effbot            | 3.22 ms                                                             | 3.42 ms: 1.06x slower                                                             |
| python_startup_no_site  | 5.80 ms                                                             | 6.53 ms: 1.13x slower                                                             |
| dask                    | 437 ms                                                              | 515 ms: 1.18x slower                                                              |
| pickle_dict             | 27.8 us                                                             | 33.3 us: 1.20x slower                                                             |
| gc_traversal            | 3.53 ms                                                             | 4.31 ms: 1.22x slower                                                             |
| coverage                | 70.6 ms                                                             | 98.3 ms: 1.39x slower                                                             |
| Geometric mean          | (ref)                                                               | 1.28x faster                                                                      |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120.json: flaskblogging, pylint
