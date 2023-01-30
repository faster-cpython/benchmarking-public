
# Results vs. 3.10.4

- fork: iritkatriel
- ref: single_arg_exit
- machine: linux-x86_64
- commit hash: 00b5a0c
- commit date: 2023-01-27
- overall geometric mean: 1.29x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-00b5a0c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 332 ms                                                 | 254 ms: 1.31x faster                                                   |
| chameleon      | 8.86 ms                                                | 6.42 ms: 1.38x faster                                                  |
| docutils       | 3.18 sec                                               | 2.51 sec: 1.27x faster                                                 |
| html5lib       | 85.8 ms                                                | 60.6 ms: 1.42x faster                                                  |
| tornado_http   | 128 ms                                                 | 94.7 ms: 1.36x faster                                                  |
| Geometric mean | (ref)                                                  | 1.34x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-00b5a0c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 108 ms                                                 | 72.5 ms: 1.49x faster                                                  |
| nbody          | 136 ms                                                 | 94.8 ms: 1.44x faster                                                  |
| pidigits       | 190 ms                                                 | 189 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.29x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-00b5a0c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 174 ms                                                 | 129 ms: 1.35x faster                                                   |
| regex_v8       | 25.0 ms                                                | 21.5 ms: 1.16x faster                                                  |
| regex_dna      | 214 ms                                                 | 205 ms: 1.04x faster                                                   |
| regex_effbot   | 3.21 ms                                                | 3.37 ms: 1.05x slower                                                  |
| Geometric mean | (ref)                                                  | 1.12x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-00b5a0c |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 453 us                                                 | 285 us: 1.59x faster                                                   |
| unpickle_pure_python | 297 us                                                 | 201 us: 1.48x faster                                                   |
| json_dumps           | 13.5 ms                                                | 9.32 ms: 1.45x faster                                                  |
| xml_etree_process    | 74.5 ms                                                | 53.5 ms: 1.39x faster                                                  |
| xml_etree_generate   | 93.3 ms                                                | 77.8 ms: 1.20x faster                                                  |
| json_loads           | 28.9 us                                                | 25.7 us: 1.12x faster                                                  |
| xml_etree_parse      | 163 ms                                                 | 146 ms: 1.12x faster                                                   |
| unpickle             | 14.3 us                                                | 13.0 us: 1.10x faster                                                  |
| pickle_list          | 4.50 us                                                | 4.15 us: 1.09x faster                                                  |
| xml_etree_iterparse  | 110 ms                                                 | 102 ms: 1.08x faster                                                   |
| unpickle_list        | 4.99 us                                                | 4.95 us: 1.01x faster                                                  |
| pickle               | 10.1 us                                                | 10.2 us: 1.01x slower                                                  |
| pickle_dict          | 28.3 us                                                | 31.3 us: 1.11x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-00b5a0c |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 13.9 ms                                                | 8.96 ms: 1.55x faster                                                  |
| python_startup_no_site | 5.76 ms                                                | 6.54 ms: 1.13x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.17x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-00b5a0c |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 14.3 ms                                                | 9.45 ms: 1.51x faster                                                  |
| genshi_text     | 30.6 ms                                                | 20.4 ms: 1.50x faster                                                  |
| django_template | 46.3 ms                                                | 33.3 ms: 1.39x faster                                                  |
| genshi_xml      | 63.6 ms                                                | 46.7 ms: 1.36x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-00b5a0c |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deltablue               | 7.39 ms                                                | 3.25 ms: 2.28x faster                                                  |
| logging_silent          | 173 ns                                                 | 92.0 ns: 1.88x faster                                                  |
| scimark_sor             | 193 ms                                                 | 107 ms: 1.80x faster                                                   |
| pyflate                 | 675 ms                                                 | 394 ms: 1.71x faster                                                   |
| richards                | 71.4 ms                                                | 42.4 ms: 1.68x faster                                                  |
| go                      | 226 ms                                                 | 138 ms: 1.64x faster                                                   |
| raytrace                | 461 ms                                                 | 283 ms: 1.63x faster                                                   |
| crypto_pyaes            | 118 ms                                                 | 73.1 ms: 1.61x faster                                                  |
| pickle_pure_python      | 453 us                                                 | 285 us: 1.59x faster                                                   |
| hexiom                  | 9.42 ms                                                | 5.98 ms: 1.58x faster                                                  |
| mypy                    | 1.01 sec                                               | 647 ms: 1.57x faster                                                   |
| scimark_monte_carlo     | 105 ms                                                 | 67.1 ms: 1.56x faster                                                  |
| python_startup          | 13.9 ms                                                | 8.96 ms: 1.55x faster                                                  |
| spectral_norm           | 148 ms                                                 | 95.4 ms: 1.55x faster                                                  |
| chaos                   | 104 ms                                                 | 67.2 ms: 1.55x faster                                                  |
| mako                    | 14.3 ms                                                | 9.45 ms: 1.51x faster                                                  |
| genshi_text             | 30.6 ms                                                | 20.4 ms: 1.50x faster                                                  |
| float                   | 108 ms                                                 | 72.5 ms: 1.49x faster                                                  |
| deepcopy_memo           | 50.0 us                                                | 33.8 us: 1.48x faster                                                  |
| unpickle_pure_python    | 297 us                                                 | 201 us: 1.48x faster                                                   |
| json_dumps              | 13.5 ms                                                | 9.32 ms: 1.45x faster                                                  |
| sqlglot_parse           | 2.04 ms                                                | 1.41 ms: 1.44x faster                                                  |
| nbody                   | 136 ms                                                 | 94.8 ms: 1.44x faster                                                  |
| pprint_pformat          | 1.97 sec                                               | 1.38 sec: 1.43x faster                                                 |
| html5lib                | 85.8 ms                                                | 60.6 ms: 1.42x faster                                                  |
| sqlglot_transpile       | 2.42 ms                                                | 1.71 ms: 1.41x faster                                                  |
| scimark_lu              | 158 ms                                                 | 112 ms: 1.41x faster                                                   |
| pprint_safe_repr        | 943 ms                                                 | 671 ms: 1.40x faster                                                   |
| xml_etree_process       | 74.5 ms                                                | 53.5 ms: 1.39x faster                                                  |
| django_template         | 46.3 ms                                                | 33.3 ms: 1.39x faster                                                  |
| logging_format          | 8.92 us                                                | 6.45 us: 1.38x faster                                                  |
| chameleon               | 8.86 ms                                                | 6.42 ms: 1.38x faster                                                  |
| async_tree_none         | 713 ms                                                 | 517 ms: 1.38x faster                                                   |
| thrift                  | 1.03 ms                                                | 749 us: 1.38x faster                                                   |
| logging_simple          | 8.06 us                                                | 5.87 us: 1.37x faster                                                  |
| genshi_xml              | 63.6 ms                                                | 46.7 ms: 1.36x faster                                                  |
| unpack_sequence         | 59.5 ns                                                | 43.8 ns: 1.36x faster                                                  |
| tornado_http            | 128 ms                                                 | 94.7 ms: 1.36x faster                                                  |
| regex_compile           | 174 ms                                                 | 129 ms: 1.35x faster                                                   |
| async_tree_io           | 1.78 sec                                               | 1.32 sec: 1.35x faster                                                 |
| pycparser               | 1.51 sec                                               | 1.12 sec: 1.34x faster                                                 |
| scimark_fft             | 414 ms                                                 | 311 ms: 1.33x faster                                                   |
| async_tree_memoization  | 854 ms                                                 | 646 ms: 1.32x faster                                                   |
| scimark_sparse_mat_mult | 5.48 ms                                                | 4.17 ms: 1.32x faster                                                  |
| aiohttp                 | 1.34 ms                                                | 1.02 ms: 1.31x faster                                                  |
| 2to3                    | 332 ms                                                 | 254 ms: 1.31x faster                                                   |
| deepcopy                | 429 us                                                 | 330 us: 1.30x faster                                                   |
| nqueens                 | 99.3 ms                                                | 76.3 ms: 1.30x faster                                                  |
| gunicorn                | 1.43 ms                                                | 1.10 ms: 1.30x faster                                                  |
| deepcopy_reduce         | 3.75 us                                                | 2.92 us: 1.29x faster                                                  |
| async_tree_cpu_io_mixed | 949 ms                                                 | 747 ms: 1.27x faster                                                   |
| docutils                | 3.18 sec                                               | 2.51 sec: 1.27x faster                                                 |
| coroutines              | 31.7 ms                                                | 25.2 ms: 1.26x faster                                                  |
| sqlglot_optimize        | 65.3 ms                                                | 52.1 ms: 1.25x faster                                                  |
| sqlglot_normalize       | 135 ms                                                 | 108 ms: 1.25x faster                                                   |
| fannkuch                | 477 ms                                                 | 381 ms: 1.25x faster                                                   |
| async_generators        | 428 ms                                                 | 352 ms: 1.22x faster                                                   |
| dulwich_log             | 75.5 ms                                                | 62.7 ms: 1.20x faster                                                  |
| sympy_integrate         | 23.9 ms                                                | 20.0 ms: 1.20x faster                                                  |
| xml_etree_generate      | 93.3 ms                                                | 77.8 ms: 1.20x faster                                                  |
| sympy_str               | 324 ms                                                 | 273 ms: 1.19x faster                                                   |
| sympy_sum               | 183 ms                                                 | 156 ms: 1.18x faster                                                   |
| sympy_expand            | 537 ms                                                 | 461 ms: 1.16x faster                                                   |
| regex_v8                | 25.0 ms                                                | 21.5 ms: 1.16x faster                                                  |
| mdp                     | 2.82 sec                                               | 2.47 sec: 1.14x faster                                                 |
| json_loads              | 28.9 us                                                | 25.7 us: 1.12x faster                                                  |
| sqlite_synth            | 2.90 us                                                | 2.59 us: 1.12x faster                                                  |
| json                    | 5.35 ms                                                | 4.78 ms: 1.12x faster                                                  |
| xml_etree_parse         | 163 ms                                                 | 146 ms: 1.12x faster                                                   |
| pathlib                 | 20.0 ms                                                | 18.0 ms: 1.12x faster                                                  |
| unpickle                | 14.3 us                                                | 13.0 us: 1.10x faster                                                  |
| meteor_contest          | 114 ms                                                 | 105 ms: 1.09x faster                                                   |
| pickle_list             | 4.50 us                                                | 4.15 us: 1.09x faster                                                  |
| xml_etree_iterparse     | 110 ms                                                 | 102 ms: 1.08x faster                                                   |
| telco                   | 6.68 ms                                                | 6.25 ms: 1.07x faster                                                  |
| regex_dna               | 214 ms                                                 | 205 ms: 1.04x faster                                                   |
| unpickle_list           | 4.99 us                                                | 4.95 us: 1.01x faster                                                  |
| pidigits                | 190 ms                                                 | 189 ms: 1.01x faster                                                   |
| pickle                  | 10.1 us                                                | 10.2 us: 1.01x slower                                                  |
| generators              | 75.8 ms                                                | 78.4 ms: 1.04x slower                                                  |
| regex_effbot            | 3.21 ms                                                | 3.37 ms: 1.05x slower                                                  |
| pickle_dict             | 28.3 us                                                | 31.3 us: 1.11x slower                                                  |
| python_startup_no_site  | 5.76 ms                                                | 6.54 ms: 1.13x slower                                                  |
| bench_mp_pool           | 24.0 ms                                                | 30.6 ms: 1.27x slower                                                  |
| coverage                | 75.3 ms                                                | 99.4 ms: 1.32x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.29x faster                                                           |

Benchmark hidden because not significant (1): bench_thread_pool
Ignored benchmarks (4) of /home/mdboom/Work/builds/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of /home/mdboom/Work/builds/benchmarking/results/bm-20230127-3.12.0a4+-00b5a0c/bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-00b5a0c.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
