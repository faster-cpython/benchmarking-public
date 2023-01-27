
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
| 2to3           | 332 ms                                                 | 251 ms: 1.32x faster                                                   |
| chameleon      | 8.86 ms                                                | 6.28 ms: 1.41x faster                                                  |
| docutils       | 3.18 sec                                               | 2.50 sec: 1.27x faster                                                 |
| html5lib       | 85.8 ms                                                | 60.2 ms: 1.42x faster                                                  |
| tornado_http   | 128 ms                                                 | 93.9 ms: 1.37x faster                                                  |
| Geometric mean | (ref)                                                  | 1.36x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-f23eec9 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 108 ms                                                 | 71.7 ms: 1.50x faster                                                  |
| nbody          | 136 ms                                                 | 94.0 ms: 1.45x faster                                                  |
| pidigits       | 190 ms                                                 | 198 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                  | 1.28x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-f23eec9 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 174 ms                                                 | 129 ms: 1.35x faster                                                   |
| regex_dna      | 214 ms                                                 | 210 ms: 1.02x faster                                                   |
| regex_effbot   | 3.21 ms                                                | 3.57 ms: 1.11x slower                                                  |
| regex_v8       | 25.0 ms                                                | 26.0 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-f23eec9 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 13.5 ms                                                | 9.38 ms: 1.44x faster                                                  |
| json_loads           | 28.9 us                                                | 24.0 us: 1.20x faster                                                  |
| pickle               | 10.1 us                                                | 10.1 us: 1.01x faster                                                  |
| pickle_dict          | 28.3 us                                                | 30.8 us: 1.09x slower                                                  |
| pickle_list          | 4.50 us                                                | 4.03 us: 1.12x faster                                                  |
| pickle_pure_python   | 453 us                                                 | 282 us: 1.61x faster                                                   |
| unpickle             | 14.3 us                                                | 13.1 us: 1.09x faster                                                  |
| unpickle_list        | 4.99 us                                                | 5.04 us: 1.01x slower                                                  |
| unpickle_pure_python | 297 us                                                 | 198 us: 1.50x faster                                                   |
| xml_etree_parse      | 163 ms                                                 | 147 ms: 1.11x faster                                                   |
| xml_etree_iterparse  | 110 ms                                                 | 102 ms: 1.08x faster                                                   |
| xml_etree_generate   | 93.3 ms                                                | 77.3 ms: 1.21x faster                                                  |
| xml_etree_process    | 74.5 ms                                                | 53.7 ms: 1.39x faster                                                  |
| Geometric mean       | (ref)                                                  | 1.19x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-f23eec9 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 13.9 ms                                                | 8.90 ms: 1.57x faster                                                  |
| python_startup_no_site | 5.76 ms                                                | 6.45 ms: 1.12x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-f23eec9 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 46.3 ms                                                | 32.8 ms: 1.41x faster                                                  |
| genshi_text     | 30.6 ms                                                | 20.7 ms: 1.48x faster                                                  |
| genshi_xml      | 63.6 ms                                                | 46.5 ms: 1.37x faster                                                  |
| mako            | 14.3 ms                                                | 9.71 ms: 1.47x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-f23eec9 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3                    | 332 ms                                                 | 251 ms: 1.32x faster                                                   |
| aiohttp                 | 1.34 ms                                                | 995 us: 1.34x faster                                                   |
| async_generators        | 428 ms                                                 | 352 ms: 1.21x faster                                                   |
| async_tree_none         | 713 ms                                                 | 524 ms: 1.36x faster                                                   |
| async_tree_cpu_io_mixed | 949 ms                                                 | 758 ms: 1.25x faster                                                   |
| async_tree_io           | 1.78 sec                                               | 1.32 sec: 1.34x faster                                                 |
| async_tree_memoization  | 854 ms                                                 | 645 ms: 1.32x faster                                                   |
| chameleon               | 8.86 ms                                                | 6.28 ms: 1.41x faster                                                  |
| chaos                   | 104 ms                                                 | 64.9 ms: 1.60x faster                                                  |
| bench_thread_pool       | 943 us                                                 | 776 us: 1.21x faster                                                   |
| coroutines              | 31.7 ms                                                | 24.5 ms: 1.29x faster                                                  |
| coverage                | 75.3 ms                                                | 97.2 ms: 1.29x slower                                                  |
| crypto_pyaes            | 118 ms                                                 | 73.0 ms: 1.61x faster                                                  |
| deepcopy                | 429 us                                                 | 334 us: 1.29x faster                                                   |
| deepcopy_reduce         | 3.75 us                                                | 2.98 us: 1.26x faster                                                  |
| deepcopy_memo           | 50.0 us                                                | 34.8 us: 1.44x faster                                                  |
| deltablue               | 7.39 ms                                                | 3.21 ms: 2.30x faster                                                  |
| django_template         | 46.3 ms                                                | 32.8 ms: 1.41x faster                                                  |
| docutils                | 3.18 sec                                               | 2.50 sec: 1.27x faster                                                 |
| dulwich_log             | 75.5 ms                                                | 62.6 ms: 1.21x faster                                                  |
| fannkuch                | 477 ms                                                 | 363 ms: 1.32x faster                                                   |
| float                   | 108 ms                                                 | 71.7 ms: 1.50x faster                                                  |
| generators              | 75.8 ms                                                | 77.4 ms: 1.02x slower                                                  |
| genshi_text             | 30.6 ms                                                | 20.7 ms: 1.48x faster                                                  |
| genshi_xml              | 63.6 ms                                                | 46.5 ms: 1.37x faster                                                  |
| go                      | 226 ms                                                 | 137 ms: 1.65x faster                                                   |
| gunicorn                | 1.43 ms                                                | 1.06 ms: 1.35x faster                                                  |
| hexiom                  | 9.42 ms                                                | 6.00 ms: 1.57x faster                                                  |
| html5lib                | 85.8 ms                                                | 60.2 ms: 1.42x faster                                                  |
| json                    | 5.35 ms                                                | 4.56 ms: 1.17x faster                                                  |
| json_dumps              | 13.5 ms                                                | 9.38 ms: 1.44x faster                                                  |
| json_loads              | 28.9 us                                                | 24.0 us: 1.20x faster                                                  |
| logging_format          | 8.92 us                                                | 6.19 us: 1.44x faster                                                  |
| logging_silent          | 173 ns                                                 | 94.9 ns: 1.83x faster                                                  |
| logging_simple          | 8.06 us                                                | 5.62 us: 1.43x faster                                                  |
| mako                    | 14.3 ms                                                | 9.71 ms: 1.47x faster                                                  |
| mdp                     | 2.82 sec                                               | 2.56 sec: 1.10x faster                                                 |
| meteor_contest          | 114 ms                                                 | 104 ms: 1.10x faster                                                   |
| mypy                    | 1.01 sec                                               | 806 ms: 1.26x faster                                                   |
| nbody                   | 136 ms                                                 | 94.0 ms: 1.45x faster                                                  |
| nqueens                 | 99.3 ms                                                | 76.3 ms: 1.30x faster                                                  |
| pathlib                 | 20.0 ms                                                | 17.7 ms: 1.13x faster                                                  |
| pickle                  | 10.1 us                                                | 10.1 us: 1.01x faster                                                  |
| pickle_dict             | 28.3 us                                                | 30.8 us: 1.09x slower                                                  |
| pickle_list             | 4.50 us                                                | 4.03 us: 1.12x faster                                                  |
| pickle_pure_python      | 453 us                                                 | 282 us: 1.61x faster                                                   |
| pidigits                | 190 ms                                                 | 198 ms: 1.04x slower                                                   |
| pprint_safe_repr        | 943 ms                                                 | 678 ms: 1.39x faster                                                   |
| pprint_pformat          | 1.97 sec                                               | 1.39 sec: 1.42x faster                                                 |
| pycparser               | 1.51 sec                                               | 1.14 sec: 1.33x faster                                                 |
| pyflate                 | 675 ms                                                 | 399 ms: 1.69x faster                                                   |
| python_startup          | 13.9 ms                                                | 8.90 ms: 1.57x faster                                                  |
| python_startup_no_site  | 5.76 ms                                                | 6.45 ms: 1.12x slower                                                  |
| raytrace                | 461 ms                                                 | 282 ms: 1.64x faster                                                   |
| regex_compile           | 174 ms                                                 | 129 ms: 1.35x faster                                                   |
| regex_dna               | 214 ms                                                 | 210 ms: 1.02x faster                                                   |
| regex_effbot            | 3.21 ms                                                | 3.57 ms: 1.11x slower                                                  |
| regex_v8                | 25.0 ms                                                | 26.0 ms: 1.04x slower                                                  |
| richards                | 71.4 ms                                                | 42.5 ms: 1.68x faster                                                  |
| scimark_fft             | 414 ms                                                 | 303 ms: 1.37x faster                                                   |
| scimark_lu              | 158 ms                                                 | 107 ms: 1.48x faster                                                   |
| scimark_monte_carlo     | 105 ms                                                 | 65.8 ms: 1.59x faster                                                  |
| scimark_sor             | 193 ms                                                 | 106 ms: 1.83x faster                                                   |
| scimark_sparse_mat_mult | 5.48 ms                                                | 4.02 ms: 1.36x faster                                                  |
| spectral_norm           | 148 ms                                                 | 100 ms: 1.48x faster                                                   |
| sqlglot_parse           | 2.04 ms                                                | 1.41 ms: 1.44x faster                                                  |
| sqlglot_transpile       | 2.42 ms                                                | 1.70 ms: 1.42x faster                                                  |
| sqlglot_optimize        | 65.3 ms                                                | 51.3 ms: 1.27x faster                                                  |
| sqlglot_normalize       | 135 ms                                                 | 105 ms: 1.29x faster                                                   |
| sqlite_synth            | 2.90 us                                                | 2.58 us: 1.12x faster                                                  |
| sympy_expand            | 537 ms                                                 | 453 ms: 1.19x faster                                                   |
| sympy_integrate         | 23.9 ms                                                | 19.7 ms: 1.21x faster                                                  |
| sympy_sum               | 183 ms                                                 | 155 ms: 1.18x faster                                                   |
| sympy_str               | 324 ms                                                 | 270 ms: 1.20x faster                                                   |
| telco                   | 6.68 ms                                                | 6.39 ms: 1.05x faster                                                  |
| thrift                  | 1.03 ms                                                | 750 us: 1.38x faster                                                   |
| tornado_http            | 128 ms                                                 | 93.9 ms: 1.37x faster                                                  |
| unpack_sequence         | 59.5 ns                                                | 44.0 ns: 1.35x faster                                                  |
| unpickle                | 14.3 us                                                | 13.1 us: 1.09x faster                                                  |
| unpickle_list           | 4.99 us                                                | 5.04 us: 1.01x slower                                                  |
| unpickle_pure_python    | 297 us                                                 | 198 us: 1.50x faster                                                   |
| xml_etree_parse         | 163 ms                                                 | 147 ms: 1.11x faster                                                   |
| xml_etree_iterparse     | 110 ms                                                 | 102 ms: 1.08x faster                                                   |
| xml_etree_generate      | 93.3 ms                                                | 77.3 ms: 1.21x faster                                                  |
| xml_etree_process       | 74.5 ms                                                | 53.7 ms: 1.39x faster                                                  |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                           |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (4) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20230127-3.12.0a4+-f23eec9/bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-f23eec9.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
