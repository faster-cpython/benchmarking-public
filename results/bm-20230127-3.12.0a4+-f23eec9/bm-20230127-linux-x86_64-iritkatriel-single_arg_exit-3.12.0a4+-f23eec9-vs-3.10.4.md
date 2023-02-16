
# Results vs. 3.10.4

- fork: iritkatriel
- ref: single_arg_exit
- machine: linux-x86_64
- commit hash: f23eec9
- commit date: 2023-01-27
- overall geometric mean: 1.30x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-f23eec9 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 251 ms: 1.33x faster                                                   |
| chameleon      | 9.17 ms                                                | 6.28 ms: 1.46x faster                                                  |
| docutils       | 3.18 sec                                               | 2.50 sec: 1.27x faster                                                 |
| html5lib       | 85.9 ms                                                | 60.2 ms: 1.43x faster                                                  |
| tornado_http   | 128 ms                                                 | 93.9 ms: 1.37x faster                                                  |
| Geometric mean | (ref)                                                  | 1.37x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-f23eec9 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 94.0 ms: 1.53x faster                                                  |
| float          | 109 ms                                                 | 71.7 ms: 1.52x faster                                                  |
| pidigits       | 190 ms                                                 | 198 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                  | 1.31x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-f23eec9 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 129 ms: 1.38x faster                                                   |
| regex_dna      | 214 ms                                                 | 210 ms: 1.02x faster                                                   |
| regex_v8       | 25.0 ms                                                | 26.0 ms: 1.04x slower                                                  |
| regex_effbot   | 3.19 ms                                                | 3.57 ms: 1.12x slower                                                  |
| Geometric mean | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-f23eec9 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 282 us: 1.60x faster                                                   |
| unpickle_pure_python | 302 us                                                 | 198 us: 1.52x faster                                                   |
| json_dumps           | 13.4 ms                                                | 9.38 ms: 1.43x faster                                                  |
| xml_etree_process    | 74.5 ms                                                | 53.7 ms: 1.39x faster                                                  |
| xml_etree_generate   | 93.8 ms                                                | 77.3 ms: 1.21x faster                                                  |
| json_loads           | 28.7 us                                                | 24.0 us: 1.20x faster                                                  |
| pickle_list          | 4.72 us                                                | 4.03 us: 1.17x faster                                                  |
| xml_etree_parse      | 163 ms                                                 | 147 ms: 1.11x faster                                                   |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.09x faster                                                   |
| unpickle             | 14.2 us                                                | 13.1 us: 1.08x faster                                                  |
| pickle               | 10.2 us                                                | 10.1 us: 1.01x faster                                                  |
| unpickle_list        | 4.92 us                                                | 5.04 us: 1.02x slower                                                  |
| pickle_dict          | 27.6 us                                                | 30.8 us: 1.12x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.19x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-f23eec9 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.90 ms: 1.58x faster                                                  |
| python_startup_no_site | 5.78 ms                                                | 6.45 ms: 1.12x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-f23eec9 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.71 ms: 1.51x faster                                                  |
| genshi_text     | 30.6 ms                                                | 20.7 ms: 1.48x faster                                                  |
| django_template | 46.3 ms                                                | 32.8 ms: 1.41x faster                                                  |
| genshi_xml      | 63.7 ms                                                | 46.5 ms: 1.37x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-f23eec9 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.21 ms: 2.27x faster                                                  |
| scimark_sor             | 197 ms                                                 | 106 ms: 1.86x faster                                                   |
| logging_silent          | 176 ns                                                 | 94.9 ns: 1.86x faster                                                  |
| asyncio_tcp             | 914 ms                                                 | 498 ms: 1.84x faster                                                   |
| richards                | 75.2 ms                                                | 42.5 ms: 1.77x faster                                                  |
| pyflate                 | 676 ms                                                 | 399 ms: 1.69x faster                                                   |
| raytrace                | 467 ms                                                 | 282 ms: 1.66x faster                                                   |
| scimark_monte_carlo     | 109 ms                                                 | 65.8 ms: 1.65x faster                                                  |
| go                      | 226 ms                                                 | 137 ms: 1.65x faster                                                   |
| chaos                   | 106 ms                                                 | 64.9 ms: 1.63x faster                                                  |
| pickle_pure_python      | 452 us                                                 | 282 us: 1.60x faster                                                   |
| crypto_pyaes            | 117 ms                                                 | 73.0 ms: 1.60x faster                                                  |
| python_startup          | 14.1 ms                                                | 8.90 ms: 1.58x faster                                                  |
| hexiom                  | 9.43 ms                                                | 6.00 ms: 1.57x faster                                                  |
| nbody                   | 144 ms                                                 | 94.0 ms: 1.53x faster                                                  |
| unpickle_pure_python    | 302 us                                                 | 198 us: 1.52x faster                                                   |
| float                   | 109 ms                                                 | 71.7 ms: 1.52x faster                                                  |
| mako                    | 14.7 ms                                                | 9.71 ms: 1.51x faster                                                  |
| scimark_lu              | 161 ms                                                 | 107 ms: 1.50x faster                                                   |
| spectral_norm           | 150 ms                                                 | 100 ms: 1.49x faster                                                   |
| deepcopy_memo           | 51.7 us                                                | 34.8 us: 1.49x faster                                                  |
| genshi_text             | 30.6 ms                                                | 20.7 ms: 1.48x faster                                                  |
| chameleon               | 9.17 ms                                                | 6.28 ms: 1.46x faster                                                  |
| sqlglot_parse           | 2.04 ms                                                | 1.41 ms: 1.45x faster                                                  |
| logging_simple          | 8.10 us                                                | 5.62 us: 1.44x faster                                                  |
| json_dumps              | 13.4 ms                                                | 9.38 ms: 1.43x faster                                                  |
| logging_format          | 8.85 us                                                | 6.19 us: 1.43x faster                                                  |
| pprint_pformat          | 1.98 sec                                               | 1.39 sec: 1.43x faster                                                 |
| html5lib                | 85.9 ms                                                | 60.2 ms: 1.43x faster                                                  |
| sqlglot_transpile       | 2.43 ms                                                | 1.70 ms: 1.42x faster                                                  |
| django_template         | 46.3 ms                                                | 32.8 ms: 1.41x faster                                                  |
| pprint_safe_repr        | 953 ms                                                 | 678 ms: 1.41x faster                                                   |
| scimark_fft             | 421 ms                                                 | 303 ms: 1.39x faster                                                   |
| xml_etree_process       | 74.5 ms                                                | 53.7 ms: 1.39x faster                                                  |
| thrift                  | 1.03 ms                                                | 750 us: 1.38x faster                                                   |
| regex_compile           | 177 ms                                                 | 129 ms: 1.38x faster                                                   |
| genshi_xml              | 63.7 ms                                                | 46.5 ms: 1.37x faster                                                  |
| tornado_http            | 128 ms                                                 | 93.9 ms: 1.37x faster                                                  |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.02 ms: 1.36x faster                                                  |
| async_tree_none         | 711 ms                                                 | 524 ms: 1.36x faster                                                   |
| unpack_sequence         | 59.4 ns                                                | 44.0 ns: 1.35x faster                                                  |
| aiohttp                 | 1.34 ms                                                | 995 us: 1.35x faster                                                   |
| async_tree_io           | 1.78 sec                                               | 1.32 sec: 1.35x faster                                                 |
| fannkuch                | 488 ms                                                 | 363 ms: 1.34x faster                                                   |
| pycparser               | 1.53 sec                                               | 1.14 sec: 1.34x faster                                                 |
| gunicorn                | 1.43 ms                                                | 1.06 ms: 1.34x faster                                                  |
| 2to3                    | 335 ms                                                 | 251 ms: 1.33x faster                                                   |
| async_tree_memoization  | 855 ms                                                 | 645 ms: 1.33x faster                                                   |
| deepcopy                | 438 us                                                 | 334 us: 1.31x faster                                                   |
| nqueens                 | 100 ms                                                 | 76.3 ms: 1.31x faster                                                  |
| coroutines              | 31.6 ms                                                | 24.5 ms: 1.29x faster                                                  |
| sqlglot_normalize       | 134 ms                                                 | 105 ms: 1.28x faster                                                   |
| deepcopy_reduce         | 3.79 us                                                | 2.98 us: 1.27x faster                                                  |
| sqlglot_optimize        | 65.2 ms                                                | 51.3 ms: 1.27x faster                                                  |
| docutils                | 3.18 sec                                               | 2.50 sec: 1.27x faster                                                 |
| async_tree_cpu_io_mixed | 949 ms                                                 | 758 ms: 1.25x faster                                                   |
| bench_thread_pool       | 946 us                                                 | 776 us: 1.22x faster                                                   |
| sympy_integrate         | 24.0 ms                                                | 19.7 ms: 1.22x faster                                                  |
| xml_etree_generate      | 93.8 ms                                                | 77.3 ms: 1.21x faster                                                  |
| dulwich_log             | 75.8 ms                                                | 62.6 ms: 1.21x faster                                                  |
| async_generators        | 426 ms                                                 | 352 ms: 1.21x faster                                                   |
| sympy_str               | 325 ms                                                 | 270 ms: 1.20x faster                                                   |
| json_loads              | 28.7 us                                                | 24.0 us: 1.20x faster                                                  |
| sympy_sum               | 183 ms                                                 | 155 ms: 1.18x faster                                                   |
| sympy_expand            | 534 ms                                                 | 453 ms: 1.18x faster                                                   |
| json                    | 5.35 ms                                                | 4.56 ms: 1.17x faster                                                  |
| pickle_list             | 4.72 us                                                | 4.03 us: 1.17x faster                                                  |
| sqlite_synth            | 2.92 us                                                | 2.58 us: 1.13x faster                                                  |
| create_gc_cycles        | 1.65 ms                                                | 1.46 ms: 1.13x faster                                                  |
| pathlib                 | 20.0 ms                                                | 17.7 ms: 1.13x faster                                                  |
| djangocms               | 36.9 us                                                | 32.8 us: 1.13x faster                                                  |
| xml_etree_parse         | 163 ms                                                 | 147 ms: 1.11x faster                                                   |
| meteor_contest          | 114 ms                                                 | 104 ms: 1.10x faster                                                   |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.09x faster                                                   |
| unpickle                | 14.2 us                                                | 13.1 us: 1.08x faster                                                  |
| mdp                     | 2.74 sec                                               | 2.56 sec: 1.07x faster                                                 |
| telco                   | 6.73 ms                                                | 6.39 ms: 1.05x faster                                                  |
| regex_dna               | 214 ms                                                 | 210 ms: 1.02x faster                                                   |
| pickle                  | 10.2 us                                                | 10.1 us: 1.01x faster                                                  |
| generators              | 76.4 ms                                                | 77.4 ms: 1.01x slower                                                  |
| unpickle_list           | 4.92 us                                                | 5.04 us: 1.02x slower                                                  |
| regex_v8                | 25.0 ms                                                | 26.0 ms: 1.04x slower                                                  |
| pidigits                | 190 ms                                                 | 198 ms: 1.04x slower                                                   |
| python_startup_no_site  | 5.78 ms                                                | 6.45 ms: 1.12x slower                                                  |
| pickle_dict             | 27.6 us                                                | 30.8 us: 1.12x slower                                                  |
| regex_effbot            | 3.19 ms                                                | 3.57 ms: 1.12x slower                                                  |
| dask                    | 436 ms                                                 | 494 ms: 1.13x slower                                                   |
| gc_traversal            | 3.53 ms                                                | 4.29 ms: 1.22x slower                                                  |
| coverage                | 74.7 ms                                                | 97.2 ms: 1.30x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                           |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230127-3.12.0a4+-f23eec9/bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-f23eec9.json: mypy
