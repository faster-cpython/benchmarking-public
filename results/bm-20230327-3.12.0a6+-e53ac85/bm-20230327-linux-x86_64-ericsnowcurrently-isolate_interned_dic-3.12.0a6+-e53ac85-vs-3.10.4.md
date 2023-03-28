
# Results vs. 3.10.4

- fork: ericsnowcurrently
- ref: isolate_interned_dic
- machine: linux-x86_64
- commit hash: e53ac85
- commit date: 2023-03-27
- overall geometric mean: 1.30x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230327-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a6+-e53ac85 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                              | 253 ms: 1.33x faster                                                              |
| chameleon      | 9.13 ms                                                             | 6.43 ms: 1.42x faster                                                             |
| docutils       | 3.19 sec                                                            | 2.53 sec: 1.26x faster                                                            |
| html5lib       | 86.4 ms                                                             | 62.2 ms: 1.39x faster                                                             |
| tornado_http   | 129 ms                                                              | 91.5 ms: 1.41x faster                                                             |
| Geometric mean | (ref)                                                               | 1.36x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230327-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a6+-e53ac85 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 146 ms                                                              | 87.1 ms: 1.67x faster                                                             |
| float          | 110 ms                                                              | 73.8 ms: 1.49x faster                                                             |
| pidigits       | 190 ms                                                              | 188 ms: 1.01x faster                                                              |
| Geometric mean | (ref)                                                               | 1.36x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230327-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a6+-e53ac85 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                              | 134 ms: 1.32x faster                                                              |
| regex_v8       | 24.9 ms                                                             | 21.7 ms: 1.15x faster                                                             |
| regex_dna      | 213 ms                                                              | 205 ms: 1.04x faster                                                              |
| regex_effbot   | 3.22 ms                                                             | 3.73 ms: 1.16x slower                                                             |
| Geometric mean | (ref)                                                               | 1.08x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230327-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a6+-e53ac85 |
|----------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pickle_pure_python   | 457 us                                                              | 285 us: 1.60x faster                                                              |
| unpickle_pure_python | 300 us                                                              | 203 us: 1.48x faster                                                              |
| json_dumps           | 13.7 ms                                                             | 9.53 ms: 1.44x faster                                                             |
| xml_etree_process    | 74.8 ms                                                             | 55.4 ms: 1.35x faster                                                             |
| json_loads           | 29.3 us                                                             | 24.3 us: 1.21x faster                                                             |
| xml_etree_generate   | 94.9 ms                                                             | 80.2 ms: 1.18x faster                                                             |
| pickle_list          | 4.73 us                                                             | 4.13 us: 1.14x faster                                                             |
| xml_etree_iterparse  | 111 ms                                                              | 98.5 ms: 1.13x faster                                                             |
| unpickle             | 15.0 us                                                             | 13.5 us: 1.11x faster                                                             |
| xml_etree_parse      | 164 ms                                                              | 148 ms: 1.11x faster                                                              |
| pickle               | 10.2 us                                                             | 10.3 us: 1.01x slower                                                             |
| unpickle_list        | 4.94 us                                                             | 4.99 us: 1.01x slower                                                             |
| pickle_dict          | 27.8 us                                                             | 31.1 us: 1.12x slower                                                             |
| Geometric mean       | (ref)                                                               | 1.19x faster                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230327-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a6+-e53ac85 |
|------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                             | 8.85 ms: 1.60x faster                                                             |
| python_startup_no_site | 5.80 ms                                                             | 6.54 ms: 1.13x slower                                                             |
| Geometric mean         | (ref)                                                               | 1.19x faster                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230327-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a6+-e53ac85 |
|-----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                             | 9.99 ms: 1.47x faster                                                             |
| genshi_text     | 30.4 ms                                                             | 21.0 ms: 1.45x faster                                                             |
| genshi_xml      | 64.3 ms                                                             | 47.1 ms: 1.37x faster                                                             |
| django_template | 45.8 ms                                                             | 33.7 ms: 1.36x faster                                                             |
| Geometric mean  | (ref)                                                               | 1.41x faster                                                                      |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230327-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a6+-e53ac85 |
|-------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| generators              | 75.7 ms                                                             | 28.7 ms: 2.64x faster                                                             |
| deltablue               | 7.30 ms                                                             | 3.23 ms: 2.26x faster                                                             |
| asyncio_tcp             | 922 ms                                                              | 506 ms: 1.82x faster                                                              |
| logging_silent          | 169 ns                                                              | 95.2 ns: 1.77x faster                                                             |
| scimark_sor             | 198 ms                                                              | 113 ms: 1.74x faster                                                              |
| richards                | 74.2 ms                                                             | 44.0 ms: 1.69x faster                                                             |
| raytrace                | 470 ms                                                              | 280 ms: 1.68x faster                                                              |
| nbody                   | 146 ms                                                              | 87.1 ms: 1.67x faster                                                             |
| scimark_monte_carlo     | 109 ms                                                              | 66.3 ms: 1.64x faster                                                             |
| go                      | 226 ms                                                              | 140 ms: 1.62x faster                                                              |
| spectral_norm           | 150 ms                                                              | 93.1 ms: 1.61x faster                                                             |
| pickle_pure_python      | 457 us                                                              | 285 us: 1.60x faster                                                              |
| python_startup          | 14.1 ms                                                             | 8.85 ms: 1.60x faster                                                             |
| pyflate                 | 671 ms                                                              | 420 ms: 1.60x faster                                                              |
| chaos                   | 106 ms                                                              | 67.4 ms: 1.57x faster                                                             |
| crypto_pyaes            | 117 ms                                                              | 74.5 ms: 1.57x faster                                                             |
| hexiom                  | 9.50 ms                                                             | 6.08 ms: 1.56x faster                                                             |
| unpack_sequence         | 65.6 ns                                                             | 42.0 ns: 1.56x faster                                                             |
| deepcopy_memo           | 51.8 us                                                             | 34.6 us: 1.50x faster                                                             |
| float                   | 110 ms                                                              | 73.8 ms: 1.49x faster                                                             |
| unpickle_pure_python    | 300 us                                                              | 203 us: 1.48x faster                                                              |
| mako                    | 14.7 ms                                                             | 9.99 ms: 1.47x faster                                                             |
| scimark_lu              | 160 ms                                                              | 109 ms: 1.47x faster                                                              |
| sqlglot_parse           | 2.07 ms                                                             | 1.42 ms: 1.46x faster                                                             |
| genshi_text             | 30.4 ms                                                             | 21.0 ms: 1.45x faster                                                             |
| json_dumps              | 13.7 ms                                                             | 9.53 ms: 1.44x faster                                                             |
| logging_format          | 9.07 us                                                             | 6.31 us: 1.44x faster                                                             |
| sqlglot_transpile       | 2.45 ms                                                             | 1.71 ms: 1.43x faster                                                             |
| logging_simple          | 8.21 us                                                             | 5.77 us: 1.42x faster                                                             |
| chameleon               | 9.13 ms                                                             | 6.43 ms: 1.42x faster                                                             |
| tornado_http            | 129 ms                                                              | 91.5 ms: 1.41x faster                                                             |
| scimark_fft             | 425 ms                                                              | 303 ms: 1.40x faster                                                              |
| pprint_pformat          | 1.98 sec                                                            | 1.42 sec: 1.39x faster                                                            |
| html5lib                | 86.4 ms                                                             | 62.2 ms: 1.39x faster                                                             |
| pprint_safe_repr        | 953 ms                                                              | 693 ms: 1.38x faster                                                              |
| pycparser               | 1.53 sec                                                            | 1.11 sec: 1.38x faster                                                            |
| async_tree_io           | 1.78 sec                                                            | 1.30 sec: 1.37x faster                                                            |
| genshi_xml              | 64.3 ms                                                             | 47.1 ms: 1.37x faster                                                             |
| django_template         | 45.8 ms                                                             | 33.7 ms: 1.36x faster                                                             |
| coroutines              | 31.8 ms                                                             | 23.4 ms: 1.36x faster                                                             |
| xml_etree_process       | 74.8 ms                                                             | 55.4 ms: 1.35x faster                                                             |
| async_tree_none         | 713 ms                                                              | 528 ms: 1.35x faster                                                              |
| deepcopy                | 438 us                                                              | 328 us: 1.34x faster                                                              |
| aiohttp                 | 1.35 ms                                                             | 1.01 ms: 1.33x faster                                                             |
| thrift                  | 1.04 ms                                                             | 779 us: 1.33x faster                                                              |
| 2to3                    | 336 ms                                                              | 253 ms: 1.33x faster                                                              |
| scimark_sparse_mat_mult | 5.62 ms                                                             | 4.24 ms: 1.32x faster                                                             |
| regex_compile           | 177 ms                                                              | 134 ms: 1.32x faster                                                              |
| gunicorn                | 1.43 ms                                                             | 1.10 ms: 1.31x faster                                                             |
| deepcopy_reduce         | 3.80 us                                                             | 2.91 us: 1.31x faster                                                             |
| async_tree_memoization  | 853 ms                                                              | 656 ms: 1.30x faster                                                              |
| mypy2                   | 432 ms                                                              | 333 ms: 1.30x faster                                                              |
| fannkuch                | 485 ms                                                              | 375 ms: 1.29x faster                                                              |
| sqlglot_normalize       | 135 ms                                                              | 106 ms: 1.27x faster                                                              |
| async_tree_cpu_io_mixed | 944 ms                                                              | 745 ms: 1.27x faster                                                              |
| sqlglot_optimize        | 65.3 ms                                                             | 51.5 ms: 1.27x faster                                                             |
| docutils                | 3.19 sec                                                            | 2.53 sec: 1.26x faster                                                            |
| nqueens                 | 98.8 ms                                                             | 79.8 ms: 1.24x faster                                                             |
| sqlalchemy_declarative  | 166 ms                                                              | 136 ms: 1.22x faster                                                              |
| json_loads              | 29.3 us                                                             | 24.3 us: 1.21x faster                                                             |
| bench_thread_pool       | 954 us                                                              | 793 us: 1.20x faster                                                              |
| sqlalchemy_imperative   | 21.2 ms                                                             | 17.7 ms: 1.19x faster                                                             |
| dulwich_log             | 76.3 ms                                                             | 64.0 ms: 1.19x faster                                                             |
| sympy_integrate         | 24.3 ms                                                             | 20.4 ms: 1.19x faster                                                             |
| xml_etree_generate      | 94.9 ms                                                             | 80.2 ms: 1.18x faster                                                             |
| sympy_expand            | 540 ms                                                              | 461 ms: 1.17x faster                                                              |
| json                    | 5.41 ms                                                             | 4.65 ms: 1.16x faster                                                             |
| sympy_str               | 328 ms                                                              | 283 ms: 1.16x faster                                                              |
| regex_v8                | 24.9 ms                                                             | 21.7 ms: 1.15x faster                                                             |
| comprehensions          | 27.3 us                                                             | 23.8 us: 1.15x faster                                                             |
| pickle_list             | 4.73 us                                                             | 4.13 us: 1.14x faster                                                             |
| sqlite_synth            | 2.97 us                                                             | 2.61 us: 1.14x faster                                                             |
| xml_etree_iterparse     | 111 ms                                                              | 98.5 ms: 1.13x faster                                                             |
| djangocms               | 36.3 us                                                             | 32.4 us: 1.12x faster                                                             |
| meteor_contest          | 115 ms                                                              | 103 ms: 1.12x faster                                                              |
| create_gc_cycles        | 1.64 ms                                                             | 1.47 ms: 1.12x faster                                                             |
| sympy_sum               | 185 ms                                                              | 166 ms: 1.11x faster                                                              |
| unpickle                | 15.0 us                                                             | 13.5 us: 1.11x faster                                                             |
| xml_etree_parse         | 164 ms                                                              | 148 ms: 1.11x faster                                                              |
| mdp                     | 2.75 sec                                                            | 2.50 sec: 1.10x faster                                                            |
| pathlib                 | 19.8 ms                                                             | 18.1 ms: 1.10x faster                                                             |
| regex_dna               | 213 ms                                                              | 205 ms: 1.04x faster                                                              |
| telco                   | 6.67 ms                                                             | 6.53 ms: 1.02x faster                                                             |
| async_generators        | 420 ms                                                              | 413 ms: 1.02x faster                                                              |
| pidigits                | 190 ms                                                              | 188 ms: 1.01x faster                                                              |
| bench_mp_pool           | 24.0 ms                                                             | 24.0 ms: 1.00x slower                                                             |
| gc_traversal            | 3.53 ms                                                             | 3.53 ms: 1.00x slower                                                             |
| pickle                  | 10.2 us                                                             | 10.3 us: 1.01x slower                                                             |
| unpickle_list           | 4.94 us                                                             | 4.99 us: 1.01x slower                                                             |
| pickle_dict             | 27.8 us                                                             | 31.1 us: 1.12x slower                                                             |
| python_startup_no_site  | 5.80 ms                                                             | 6.54 ms: 1.13x slower                                                             |
| regex_effbot            | 3.22 ms                                                             | 3.73 ms: 1.16x slower                                                             |
| dask                    | 437 ms                                                              | 509 ms: 1.17x slower                                                              |
| coverage                | 70.6 ms                                                             | 97.3 ms: 1.38x slower                                                             |
| Geometric mean          | (ref)                                                               | 1.30x faster                                                                      |
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120.json: flaskblogging, pylint
