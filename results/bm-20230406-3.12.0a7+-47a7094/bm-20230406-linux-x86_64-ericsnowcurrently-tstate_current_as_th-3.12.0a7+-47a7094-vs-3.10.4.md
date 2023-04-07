
# Results vs. 3.10.4

- fork: ericsnowcurrently
- ref: tstate_current_as_th
- machine: linux-x86_64
- commit hash: 47a7094
- commit date: 2023-04-06
- overall geometric mean: 1.31x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230406-linux-x86_64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-47a7094 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                              | 251 ms: 1.34x faster                                                              |
| chameleon      | 9.13 ms                                                             | 6.42 ms: 1.42x faster                                                             |
| docutils       | 3.19 sec                                                            | 2.53 sec: 1.26x faster                                                            |
| html5lib       | 86.4 ms                                                             | 61.2 ms: 1.41x faster                                                             |
| tornado_http   | 129 ms                                                              | 90.3 ms: 1.43x faster                                                             |
| Geometric mean | (ref)                                                               | 1.37x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230406-linux-x86_64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-47a7094 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 146 ms                                                              | 83.6 ms: 1.74x faster                                                             |
| float          | 110 ms                                                              | 72.6 ms: 1.51x faster                                                             |
| pidigits       | 190 ms                                                              | 188 ms: 1.01x faster                                                              |
| Geometric mean | (ref)                                                               | 1.39x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230406-linux-x86_64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-47a7094 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                              | 132 ms: 1.34x faster                                                              |
| regex_v8       | 24.9 ms                                                             | 22.6 ms: 1.10x faster                                                             |
| regex_dna      | 213 ms                                                              | 214 ms: 1.00x slower                                                              |
| regex_effbot   | 3.22 ms                                                             | 3.63 ms: 1.13x slower                                                             |
| Geometric mean | (ref)                                                               | 1.07x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230406-linux-x86_64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-47a7094 |
|----------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pickle_pure_python   | 457 us                                                              | 292 us: 1.57x faster                                                              |
| unpickle_pure_python | 300 us                                                              | 201 us: 1.49x faster                                                              |
| json_dumps           | 13.7 ms                                                             | 9.46 ms: 1.45x faster                                                             |
| xml_etree_process    | 74.8 ms                                                             | 55.0 ms: 1.36x faster                                                             |
| json_loads           | 29.3 us                                                             | 24.5 us: 1.20x faster                                                             |
| xml_etree_generate   | 94.9 ms                                                             | 80.7 ms: 1.18x faster                                                             |
| xml_etree_iterparse  | 111 ms                                                              | 99.4 ms: 1.12x faster                                                             |
| xml_etree_parse      | 164 ms                                                              | 147 ms: 1.11x faster                                                              |
| unpickle             | 15.0 us                                                             | 13.6 us: 1.10x faster                                                             |
| pickle_list          | 4.73 us                                                             | 4.43 us: 1.07x faster                                                             |
| unpickle_list        | 4.94 us                                                             | 4.87 us: 1.01x faster                                                             |
| pickle               | 10.2 us                                                             | 10.6 us: 1.03x slower                                                             |
| pickle_dict          | 27.8 us                                                             | 32.3 us: 1.16x slower                                                             |
| Geometric mean       | (ref)                                                               | 1.17x faster                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230406-linux-x86_64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-47a7094 |
|------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                             | 8.87 ms: 1.59x faster                                                             |
| python_startup_no_site | 5.80 ms                                                             | 6.55 ms: 1.13x slower                                                             |
| Geometric mean         | (ref)                                                               | 1.19x faster                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230406-linux-x86_64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-47a7094 |
|-----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                             | 9.99 ms: 1.47x faster                                                             |
| genshi_text     | 30.4 ms                                                             | 21.1 ms: 1.44x faster                                                             |
| django_template | 45.8 ms                                                             | 32.0 ms: 1.43x faster                                                             |
| genshi_xml      | 64.3 ms                                                             | 47.3 ms: 1.36x faster                                                             |
| Geometric mean  | (ref)                                                               | 1.43x faster                                                                      |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230406-linux-x86_64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-47a7094 |
|-------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| generators              | 75.7 ms                                                             | 29.4 ms: 2.58x faster                                                             |
| deltablue               | 7.30 ms                                                             | 3.20 ms: 2.28x faster                                                             |
| asyncio_tcp             | 922 ms                                                              | 501 ms: 1.84x faster                                                              |
| scimark_sor             | 198 ms                                                              | 109 ms: 1.81x faster                                                              |
| logging_silent          | 169 ns                                                              | 93.5 ns: 1.81x faster                                                             |
| nbody                   | 146 ms                                                              | 83.6 ms: 1.74x faster                                                             |
| sqlglot_parse           | 2.07 ms                                                             | 1.20 ms: 1.73x faster                                                             |
| richards                | 74.2 ms                                                             | 43.1 ms: 1.72x faster                                                             |
| raytrace                | 470 ms                                                              | 275 ms: 1.71x faster                                                              |
| go                      | 226 ms                                                              | 135 ms: 1.67x faster                                                              |
| sqlglot_transpile       | 2.45 ms                                                             | 1.48 ms: 1.66x faster                                                             |
| scimark_monte_carlo     | 109 ms                                                              | 65.7 ms: 1.65x faster                                                             |
| chaos                   | 106 ms                                                              | 64.7 ms: 1.64x faster                                                             |
| pyflate                 | 671 ms                                                              | 416 ms: 1.61x faster                                                              |
| spectral_norm           | 150 ms                                                              | 93.2 ms: 1.61x faster                                                             |
| python_startup          | 14.1 ms                                                             | 8.87 ms: 1.59x faster                                                             |
| hexiom                  | 9.50 ms                                                             | 6.05 ms: 1.57x faster                                                             |
| crypto_pyaes            | 117 ms                                                              | 74.4 ms: 1.57x faster                                                             |
| pickle_pure_python      | 457 us                                                              | 292 us: 1.57x faster                                                              |
| unpack_sequence         | 65.6 ns                                                             | 42.1 ns: 1.56x faster                                                             |
| deepcopy_memo           | 51.8 us                                                             | 33.6 us: 1.54x faster                                                             |
| float                   | 110 ms                                                              | 72.6 ms: 1.51x faster                                                             |
| scimark_lu              | 160 ms                                                              | 106 ms: 1.51x faster                                                              |
| unpickle_pure_python    | 300 us                                                              | 201 us: 1.49x faster                                                              |
| mako                    | 14.7 ms                                                             | 9.99 ms: 1.47x faster                                                             |
| json_dumps              | 13.7 ms                                                             | 9.46 ms: 1.45x faster                                                             |
| logging_simple          | 8.21 us                                                             | 5.69 us: 1.44x faster                                                             |
| genshi_text             | 30.4 ms                                                             | 21.1 ms: 1.44x faster                                                             |
| logging_format          | 9.07 us                                                             | 6.31 us: 1.44x faster                                                             |
| django_template         | 45.8 ms                                                             | 32.0 ms: 1.43x faster                                                             |
| tornado_http            | 129 ms                                                              | 90.3 ms: 1.43x faster                                                             |
| pprint_pformat          | 1.98 sec                                                            | 1.39 sec: 1.43x faster                                                            |
| chameleon               | 9.13 ms                                                             | 6.42 ms: 1.42x faster                                                             |
| pprint_safe_repr        | 953 ms                                                              | 671 ms: 1.42x faster                                                              |
| html5lib                | 86.4 ms                                                             | 61.2 ms: 1.41x faster                                                             |
| async_tree_memoization  | 853 ms                                                              | 605 ms: 1.41x faster                                                              |
| async_tree_io           | 1.78 sec                                                            | 1.27 sec: 1.41x faster                                                            |
| scimark_sparse_mat_mult | 5.62 ms                                                             | 4.01 ms: 1.40x faster                                                             |
| async_tree_none         | 713 ms                                                              | 512 ms: 1.39x faster                                                              |
| scimark_fft             | 425 ms                                                              | 306 ms: 1.39x faster                                                              |
| coroutines              | 31.8 ms                                                             | 22.9 ms: 1.39x faster                                                             |
| xml_etree_process       | 74.8 ms                                                             | 55.0 ms: 1.36x faster                                                             |
| genshi_xml              | 64.3 ms                                                             | 47.3 ms: 1.36x faster                                                             |
| deepcopy                | 438 us                                                              | 324 us: 1.35x faster                                                              |
| pycparser               | 1.53 sec                                                            | 1.14 sec: 1.35x faster                                                            |
| regex_compile           | 177 ms                                                              | 132 ms: 1.34x faster                                                              |
| 2to3                    | 336 ms                                                              | 251 ms: 1.34x faster                                                              |
| aiohttp                 | 1.35 ms                                                             | 1.01 ms: 1.34x faster                                                             |
| async_tree_cpu_io_mixed | 944 ms                                                              | 715 ms: 1.32x faster                                                              |
| sqlglot_normalize       | 135 ms                                                              | 102 ms: 1.32x faster                                                              |
| thrift                  | 1.04 ms                                                             | 787 us: 1.32x faster                                                              |
| gunicorn                | 1.43 ms                                                             | 1.09 ms: 1.31x faster                                                             |
| sqlglot_optimize        | 65.3 ms                                                             | 50.3 ms: 1.30x faster                                                             |
| mypy2                   | 432 ms                                                              | 333 ms: 1.30x faster                                                              |
| deepcopy_reduce         | 3.80 us                                                             | 2.94 us: 1.29x faster                                                             |
| fannkuch                | 485 ms                                                              | 377 ms: 1.29x faster                                                              |
| comprehensions          | 27.3 us                                                             | 21.4 us: 1.27x faster                                                             |
| docutils                | 3.19 sec                                                            | 2.53 sec: 1.26x faster                                                            |
| nqueens                 | 98.8 ms                                                             | 79.4 ms: 1.25x faster                                                             |
| dulwich_log             | 76.3 ms                                                             | 62.8 ms: 1.22x faster                                                             |
| bench_thread_pool       | 954 us                                                              | 788 us: 1.21x faster                                                              |
| sqlalchemy_imperative   | 21.2 ms                                                             | 17.6 ms: 1.20x faster                                                             |
| sqlalchemy_declarative  | 166 ms                                                              | 139 ms: 1.20x faster                                                              |
| json_loads              | 29.3 us                                                             | 24.5 us: 1.20x faster                                                             |
| sympy_integrate         | 24.3 ms                                                             | 20.4 ms: 1.19x faster                                                             |
| sympy_expand            | 540 ms                                                              | 457 ms: 1.18x faster                                                              |
| xml_etree_generate      | 94.9 ms                                                             | 80.7 ms: 1.18x faster                                                             |
| sympy_str               | 328 ms                                                              | 282 ms: 1.16x faster                                                              |
| json                    | 5.41 ms                                                             | 4.73 ms: 1.14x faster                                                             |
| meteor_contest          | 115 ms                                                              | 101 ms: 1.13x faster                                                              |
| sqlite_synth            | 2.97 us                                                             | 2.63 us: 1.13x faster                                                             |
| djangocms               | 36.3 us                                                             | 32.2 us: 1.13x faster                                                             |
| sympy_sum               | 185 ms                                                              | 165 ms: 1.12x faster                                                              |
| xml_etree_iterparse     | 111 ms                                                              | 99.4 ms: 1.12x faster                                                             |
| xml_etree_parse         | 164 ms                                                              | 147 ms: 1.11x faster                                                              |
| create_gc_cycles        | 1.64 ms                                                             | 1.48 ms: 1.11x faster                                                             |
| regex_v8                | 24.9 ms                                                             | 22.6 ms: 1.10x faster                                                             |
| unpickle                | 15.0 us                                                             | 13.6 us: 1.10x faster                                                             |
| pathlib                 | 19.8 ms                                                             | 18.3 ms: 1.08x faster                                                             |
| pickle_list             | 4.73 us                                                             | 4.43 us: 1.07x faster                                                             |
| telco                   | 6.67 ms                                                             | 6.48 ms: 1.03x faster                                                             |
| async_generators        | 420 ms                                                              | 409 ms: 1.03x faster                                                              |
| mdp                     | 2.75 sec                                                            | 2.68 sec: 1.03x faster                                                            |
| unpickle_list           | 4.94 us                                                             | 4.87 us: 1.01x faster                                                             |
| pidigits                | 190 ms                                                              | 188 ms: 1.01x faster                                                              |
| bench_mp_pool           | 24.0 ms                                                             | 24.0 ms: 1.00x slower                                                             |
| regex_dna               | 213 ms                                                              | 214 ms: 1.00x slower                                                              |
| pickle                  | 10.2 us                                                             | 10.6 us: 1.03x slower                                                             |
| regex_effbot            | 3.22 ms                                                             | 3.63 ms: 1.13x slower                                                             |
| python_startup_no_site  | 5.80 ms                                                             | 6.55 ms: 1.13x slower                                                             |
| dask                    | 437 ms                                                              | 499 ms: 1.14x slower                                                              |
| pickle_dict             | 27.8 us                                                             | 32.3 us: 1.16x slower                                                             |
| gc_traversal            | 3.53 ms                                                             | 4.19 ms: 1.19x slower                                                             |
| coverage                | 70.6 ms                                                             | 96.6 ms: 1.37x slower                                                             |
| Geometric mean          | (ref)                                                               | 1.31x faster                                                                      |
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120.json: flaskblogging, pylint
