
# Results vs. 3.10.4

- fork: ericsnowcurrently
- ref: interp_current_as_th
- machine: linux-x86_64
- commit hash: fbb272a
- commit date: 2023-04-11
- overall geometric mean: 1.31x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230411-linux-x86_64-ericsnowcurrently-interp_current_as_th-3.12.0a7+-fbb272a |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                              | 250 ms: 1.34x faster                                                              |
| chameleon      | 9.13 ms                                                             | 6.51 ms: 1.40x faster                                                             |
| docutils       | 3.19 sec                                                            | 2.52 sec: 1.27x faster                                                            |
| html5lib       | 86.4 ms                                                             | 61.3 ms: 1.41x faster                                                             |
| tornado_http   | 129 ms                                                              | 90.5 ms: 1.42x faster                                                             |
| Geometric mean | (ref)                                                               | 1.37x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230411-linux-x86_64-ericsnowcurrently-interp_current_as_th-3.12.0a7+-fbb272a |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 146 ms                                                              | 82.7 ms: 1.76x faster                                                             |
| float          | 110 ms                                                              | 73.0 ms: 1.51x faster                                                             |
| pidigits       | 190 ms                                                              | 188 ms: 1.01x faster                                                              |
| Geometric mean | (ref)                                                               | 1.39x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230411-linux-x86_64-ericsnowcurrently-interp_current_as_th-3.12.0a7+-fbb272a |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                              | 131 ms: 1.35x faster                                                              |
| regex_v8       | 24.9 ms                                                             | 22.5 ms: 1.11x faster                                                             |
| regex_dna      | 213 ms                                                              | 214 ms: 1.00x slower                                                              |
| regex_effbot   | 3.22 ms                                                             | 3.57 ms: 1.11x slower                                                             |
| Geometric mean | (ref)                                                               | 1.08x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230411-linux-x86_64-ericsnowcurrently-interp_current_as_th-3.12.0a7+-fbb272a |
|----------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pickle_pure_python   | 457 us                                                              | 284 us: 1.61x faster                                                              |
| unpickle_pure_python | 300 us                                                              | 202 us: 1.49x faster                                                              |
| json_dumps           | 13.7 ms                                                             | 9.40 ms: 1.46x faster                                                             |
| xml_etree_process    | 74.8 ms                                                             | 55.3 ms: 1.35x faster                                                             |
| json_loads           | 29.3 us                                                             | 24.4 us: 1.20x faster                                                             |
| xml_etree_generate   | 94.9 ms                                                             | 80.2 ms: 1.18x faster                                                             |
| unpickle             | 15.0 us                                                             | 13.1 us: 1.14x faster                                                             |
| xml_etree_iterparse  | 111 ms                                                              | 98.7 ms: 1.13x faster                                                             |
| xml_etree_parse      | 164 ms                                                              | 150 ms: 1.09x faster                                                              |
| pickle_list          | 4.73 us                                                             | 4.34 us: 1.09x faster                                                             |
| unpickle_list        | 4.94 us                                                             | 4.67 us: 1.06x faster                                                             |
| pickle               | 10.2 us                                                             | 10.6 us: 1.04x slower                                                             |
| pickle_dict          | 27.8 us                                                             | 32.1 us: 1.16x slower                                                             |
| Geometric mean       | (ref)                                                               | 1.18x faster                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230411-linux-x86_64-ericsnowcurrently-interp_current_as_th-3.12.0a7+-fbb272a |
|------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                             | 8.80 ms: 1.61x faster                                                             |
| python_startup_no_site | 5.80 ms                                                             | 6.50 ms: 1.12x slower                                                             |
| Geometric mean         | (ref)                                                               | 1.20x faster                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230411-linux-x86_64-ericsnowcurrently-interp_current_as_th-3.12.0a7+-fbb272a |
|-----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                             | 9.95 ms: 1.48x faster                                                             |
| genshi_text     | 30.4 ms                                                             | 21.2 ms: 1.43x faster                                                             |
| django_template | 45.8 ms                                                             | 32.0 ms: 1.43x faster                                                             |
| genshi_xml      | 64.3 ms                                                             | 47.1 ms: 1.37x faster                                                             |
| Geometric mean  | (ref)                                                               | 1.43x faster                                                                      |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230411-linux-x86_64-ericsnowcurrently-interp_current_as_th-3.12.0a7+-fbb272a |
|-------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| generators              | 75.7 ms                                                             | 29.2 ms: 2.59x faster                                                             |
| deltablue               | 7.30 ms                                                             | 3.19 ms: 2.29x faster                                                             |
| asyncio_tcp             | 922 ms                                                              | 507 ms: 1.82x faster                                                              |
| scimark_sor             | 198 ms                                                              | 109 ms: 1.81x faster                                                              |
| logging_silent          | 169 ns                                                              | 94.3 ns: 1.79x faster                                                             |
| nbody                   | 146 ms                                                              | 82.7 ms: 1.76x faster                                                             |
| sqlglot_parse           | 2.07 ms                                                             | 1.20 ms: 1.72x faster                                                             |
| richards                | 74.2 ms                                                             | 43.2 ms: 1.72x faster                                                             |
| raytrace                | 470 ms                                                              | 275 ms: 1.71x faster                                                              |
| chaos                   | 106 ms                                                              | 64.1 ms: 1.65x faster                                                             |
| sqlglot_transpile       | 2.45 ms                                                             | 1.49 ms: 1.65x faster                                                             |
| scimark_monte_carlo     | 109 ms                                                              | 66.6 ms: 1.63x faster                                                             |
| go                      | 226 ms                                                              | 139 ms: 1.62x faster                                                              |
| pickle_pure_python      | 457 us                                                              | 284 us: 1.61x faster                                                              |
| python_startup          | 14.1 ms                                                             | 8.80 ms: 1.61x faster                                                             |
| pyflate                 | 671 ms                                                              | 419 ms: 1.60x faster                                                              |
| spectral_norm           | 150 ms                                                              | 94.1 ms: 1.60x faster                                                             |
| hexiom                  | 9.50 ms                                                             | 5.99 ms: 1.59x faster                                                             |
| crypto_pyaes            | 117 ms                                                              | 73.8 ms: 1.58x faster                                                             |
| unpack_sequence         | 65.6 ns                                                             | 42.3 ns: 1.55x faster                                                             |
| deepcopy_memo           | 51.8 us                                                             | 33.6 us: 1.54x faster                                                             |
| scimark_lu              | 160 ms                                                              | 106 ms: 1.51x faster                                                              |
| float                   | 110 ms                                                              | 73.0 ms: 1.51x faster                                                             |
| unpickle_pure_python    | 300 us                                                              | 202 us: 1.49x faster                                                              |
| mako                    | 14.7 ms                                                             | 9.95 ms: 1.48x faster                                                             |
| logging_format          | 9.07 us                                                             | 6.18 us: 1.47x faster                                                             |
| logging_simple          | 8.21 us                                                             | 5.62 us: 1.46x faster                                                             |
| json_dumps              | 13.7 ms                                                             | 9.40 ms: 1.46x faster                                                             |
| genshi_text             | 30.4 ms                                                             | 21.2 ms: 1.43x faster                                                             |
| django_template         | 45.8 ms                                                             | 32.0 ms: 1.43x faster                                                             |
| pprint_pformat          | 1.98 sec                                                            | 1.38 sec: 1.43x faster                                                            |
| tornado_http            | 129 ms                                                              | 90.5 ms: 1.42x faster                                                             |
| scimark_fft             | 425 ms                                                              | 300 ms: 1.42x faster                                                              |
| async_tree_memoization  | 853 ms                                                              | 605 ms: 1.41x faster                                                              |
| html5lib                | 86.4 ms                                                             | 61.3 ms: 1.41x faster                                                             |
| chameleon               | 9.13 ms                                                             | 6.51 ms: 1.40x faster                                                             |
| pprint_safe_repr        | 953 ms                                                              | 682 ms: 1.40x faster                                                              |
| coroutines              | 31.8 ms                                                             | 23.0 ms: 1.38x faster                                                             |
| async_tree_io           | 1.78 sec                                                            | 1.29 sec: 1.38x faster                                                            |
| async_tree_none         | 713 ms                                                              | 516 ms: 1.38x faster                                                              |
| deepcopy                | 438 us                                                              | 321 us: 1.37x faster                                                              |
| genshi_xml              | 64.3 ms                                                             | 47.1 ms: 1.37x faster                                                             |
| scimark_sparse_mat_mult | 5.62 ms                                                             | 4.12 ms: 1.36x faster                                                             |
| xml_etree_process       | 74.8 ms                                                             | 55.3 ms: 1.35x faster                                                             |
| thrift                  | 1.04 ms                                                             | 767 us: 1.35x faster                                                              |
| regex_compile           | 177 ms                                                              | 131 ms: 1.35x faster                                                              |
| pycparser               | 1.53 sec                                                            | 1.14 sec: 1.35x faster                                                            |
| 2to3                    | 336 ms                                                              | 250 ms: 1.34x faster                                                              |
| aiohttp                 | 1.35 ms                                                             | 1.00 ms: 1.34x faster                                                             |
| sqlglot_normalize       | 135 ms                                                              | 101 ms: 1.33x faster                                                              |
| gunicorn                | 1.43 ms                                                             | 1.08 ms: 1.32x faster                                                             |
| deepcopy_reduce         | 3.80 us                                                             | 2.87 us: 1.32x faster                                                             |
| async_tree_cpu_io_mixed | 944 ms                                                              | 721 ms: 1.31x faster                                                              |
| sqlglot_optimize        | 65.3 ms                                                             | 49.9 ms: 1.31x faster                                                             |
| mypy2                   | 432 ms                                                              | 333 ms: 1.30x faster                                                              |
| comprehensions          | 27.3 us                                                             | 21.2 us: 1.28x faster                                                             |
| docutils                | 3.19 sec                                                            | 2.52 sec: 1.27x faster                                                            |
| nqueens                 | 98.8 ms                                                             | 78.8 ms: 1.25x faster                                                             |
| fannkuch                | 485 ms                                                              | 392 ms: 1.24x faster                                                              |
| dulwich_log             | 76.3 ms                                                             | 62.3 ms: 1.23x faster                                                             |
| sqlalchemy_declarative  | 166 ms                                                              | 136 ms: 1.22x faster                                                              |
| bench_thread_pool       | 954 us                                                              | 785 us: 1.22x faster                                                              |
| json_loads              | 29.3 us                                                             | 24.4 us: 1.20x faster                                                             |
| sqlalchemy_imperative   | 21.2 ms                                                             | 17.7 ms: 1.20x faster                                                             |
| sympy_integrate         | 24.3 ms                                                             | 20.3 ms: 1.20x faster                                                             |
| xml_etree_generate      | 94.9 ms                                                             | 80.2 ms: 1.18x faster                                                             |
| sympy_expand            | 540 ms                                                              | 457 ms: 1.18x faster                                                              |
| sympy_str               | 328 ms                                                              | 282 ms: 1.16x faster                                                              |
| json                    | 5.41 ms                                                             | 4.72 ms: 1.15x faster                                                             |
| sqlite_synth            | 2.97 us                                                             | 2.60 us: 1.14x faster                                                             |
| unpickle                | 15.0 us                                                             | 13.1 us: 1.14x faster                                                             |
| djangocms               | 36.3 us                                                             | 32.1 us: 1.13x faster                                                             |
| meteor_contest          | 115 ms                                                              | 101 ms: 1.13x faster                                                              |
| xml_etree_iterparse     | 111 ms                                                              | 98.7 ms: 1.13x faster                                                             |
| sympy_sum               | 185 ms                                                              | 164 ms: 1.13x faster                                                              |
| regex_v8                | 24.9 ms                                                             | 22.5 ms: 1.11x faster                                                             |
| mdp                     | 2.75 sec                                                            | 2.50 sec: 1.10x faster                                                            |
| create_gc_cycles        | 1.64 ms                                                             | 1.49 ms: 1.10x faster                                                             |
| pathlib                 | 19.8 ms                                                             | 18.0 ms: 1.10x faster                                                             |
| xml_etree_parse         | 164 ms                                                              | 150 ms: 1.09x faster                                                              |
| pickle_list             | 4.73 us                                                             | 4.34 us: 1.09x faster                                                             |
| unpickle_list           | 4.94 us                                                             | 4.67 us: 1.06x faster                                                             |
| telco                   | 6.67 ms                                                             | 6.41 ms: 1.04x faster                                                             |
| async_generators        | 420 ms                                                              | 405 ms: 1.04x faster                                                              |
| pidigits                | 190 ms                                                              | 188 ms: 1.01x faster                                                              |
| regex_dna               | 213 ms                                                              | 214 ms: 1.00x slower                                                              |
| pickle                  | 10.2 us                                                             | 10.6 us: 1.04x slower                                                             |
| regex_effbot            | 3.22 ms                                                             | 3.57 ms: 1.11x slower                                                             |
| python_startup_no_site  | 5.80 ms                                                             | 6.50 ms: 1.12x slower                                                             |
| dask                    | 437 ms                                                              | 493 ms: 1.13x slower                                                              |
| pickle_dict             | 27.8 us                                                             | 32.1 us: 1.16x slower                                                             |
| gc_traversal            | 3.53 ms                                                             | 4.30 ms: 1.22x slower                                                             |
| coverage                | 70.6 ms                                                             | 97.8 ms: 1.38x slower                                                             |
| Geometric mean          | (ref)                                                               | 1.31x faster                                                                      |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120.json: flaskblogging, pylint
