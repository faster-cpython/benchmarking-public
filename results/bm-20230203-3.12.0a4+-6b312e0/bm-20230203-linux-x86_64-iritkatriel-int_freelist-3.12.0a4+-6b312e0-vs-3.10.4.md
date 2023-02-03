
# Results vs. 3.10.4

- fork: iritkatriel
- ref: int_freelist
- machine: linux-x86_64
- commit hash: 6b312e0
- commit date: 2023-02-03
- overall geometric mean: 1.30x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-6b312e0 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 332 ms                                                 | 252 ms: 1.32x faster                                                |
| chameleon      | 8.86 ms                                                | 6.28 ms: 1.41x faster                                               |
| docutils       | 3.18 sec                                               | 2.50 sec: 1.27x faster                                              |
| html5lib       | 85.8 ms                                                | 59.5 ms: 1.44x faster                                               |
| tornado_http   | 128 ms                                                 | 94.0 ms: 1.37x faster                                               |
| Geometric mean | (ref)                                                  | 1.36x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-6b312e0 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 108 ms                                                 | 72.5 ms: 1.49x faster                                               |
| nbody          | 136 ms                                                 | 96.7 ms: 1.41x faster                                               |
| pidigits       | 190 ms                                                 | 191 ms: 1.00x slower                                                |
| Geometric mean | (ref)                                                  | 1.28x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-6b312e0 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 174 ms                                                 | 128 ms: 1.36x faster                                                |
| regex_v8       | 25.0 ms                                                | 22.6 ms: 1.10x faster                                               |
| regex_dna      | 214 ms                                                 | 208 ms: 1.03x faster                                                |
| regex_effbot   | 3.21 ms                                                | 3.44 ms: 1.07x slower                                               |
| Geometric mean | (ref)                                                  | 1.10x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-6b312e0 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_pure_python   | 453 us                                                 | 287 us: 1.58x faster                                                |
| unpickle_pure_python | 297 us                                                 | 200 us: 1.48x faster                                                |
| json_dumps           | 13.5 ms                                                | 9.52 ms: 1.42x faster                                               |
| xml_etree_process    | 74.5 ms                                                | 53.4 ms: 1.40x faster                                               |
| json_loads           | 28.9 us                                                | 23.8 us: 1.21x faster                                               |
| xml_etree_generate   | 93.3 ms                                                | 77.6 ms: 1.20x faster                                               |
| pickle_list          | 4.50 us                                                | 3.92 us: 1.15x faster                                               |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                |
| unpickle             | 14.3 us                                                | 13.1 us: 1.09x faster                                               |
| xml_etree_iterparse  | 110 ms                                                 | 102 ms: 1.08x faster                                                |
| pickle               | 10.1 us                                                | 10.0 us: 1.01x faster                                               |
| unpickle_list        | 4.99 us                                                | 5.02 us: 1.01x slower                                               |
| pickle_dict          | 28.3 us                                                | 29.8 us: 1.05x slower                                               |
| Geometric mean       | (ref)                                                  | 1.19x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-6b312e0 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 13.9 ms                                                | 8.96 ms: 1.56x faster                                               |
| python_startup_no_site | 5.76 ms                                                | 6.48 ms: 1.12x slower                                               |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-6b312e0 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 14.3 ms                                                | 9.58 ms: 1.49x faster                                               |
| genshi_text     | 30.6 ms                                                | 20.8 ms: 1.47x faster                                               |
| django_template | 46.3 ms                                                | 32.3 ms: 1.43x faster                                               |
| genshi_xml      | 63.6 ms                                                | 47.9 ms: 1.33x faster                                               |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-6b312e0 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| deltablue               | 7.39 ms                                                | 3.18 ms: 2.32x faster                                               |
| logging_silent          | 173 ns                                                 | 92.7 ns: 1.87x faster                                               |
| scimark_sor             | 193 ms                                                 | 109 ms: 1.78x faster                                                |
| go                      | 226 ms                                                 | 132 ms: 1.72x faster                                                |
| richards                | 71.4 ms                                                | 41.8 ms: 1.71x faster                                               |
| chaos                   | 104 ms                                                 | 63.5 ms: 1.64x faster                                               |
| pyflate                 | 675 ms                                                 | 414 ms: 1.63x faster                                                |
| raytrace                | 461 ms                                                 | 285 ms: 1.62x faster                                                |
| hexiom                  | 9.42 ms                                                | 5.94 ms: 1.59x faster                                               |
| pickle_pure_python      | 453 us                                                 | 287 us: 1.58x faster                                                |
| scimark_monte_carlo     | 105 ms                                                 | 66.5 ms: 1.58x faster                                               |
| python_startup          | 13.9 ms                                                | 8.96 ms: 1.56x faster                                               |
| crypto_pyaes            | 118 ms                                                 | 76.4 ms: 1.54x faster                                               |
| mako                    | 14.3 ms                                                | 9.58 ms: 1.49x faster                                               |
| float                   | 108 ms                                                 | 72.5 ms: 1.49x faster                                               |
| unpickle_pure_python    | 297 us                                                 | 200 us: 1.48x faster                                                |
| genshi_text             | 30.6 ms                                                | 20.8 ms: 1.47x faster                                               |
| scimark_lu              | 158 ms                                                 | 108 ms: 1.47x faster                                                |
| deepcopy_memo           | 50.0 us                                                | 34.2 us: 1.46x faster                                               |
| sqlglot_parse           | 2.04 ms                                                | 1.40 ms: 1.46x faster                                               |
| html5lib                | 85.8 ms                                                | 59.5 ms: 1.44x faster                                               |
| spectral_norm           | 148 ms                                                 | 103 ms: 1.44x faster                                                |
| pprint_pformat          | 1.97 sec                                               | 1.38 sec: 1.43x faster                                              |
| django_template         | 46.3 ms                                                | 32.3 ms: 1.43x faster                                               |
| sqlglot_transpile       | 2.42 ms                                                | 1.69 ms: 1.43x faster                                               |
| logging_format          | 8.92 us                                                | 6.28 us: 1.42x faster                                               |
| json_dumps              | 13.5 ms                                                | 9.52 ms: 1.42x faster                                               |
| logging_simple          | 8.06 us                                                | 5.70 us: 1.41x faster                                               |
| chameleon               | 8.86 ms                                                | 6.28 ms: 1.41x faster                                               |
| nbody                   | 136 ms                                                 | 96.7 ms: 1.41x faster                                               |
| xml_etree_process       | 74.5 ms                                                | 53.4 ms: 1.40x faster                                               |
| pprint_safe_repr        | 943 ms                                                 | 676 ms: 1.39x faster                                                |
| thrift                  | 1.03 ms                                                | 747 us: 1.38x faster                                                |
| scimark_sparse_mat_mult | 5.48 ms                                                | 3.98 ms: 1.38x faster                                               |
| tornado_http            | 128 ms                                                 | 94.0 ms: 1.37x faster                                               |
| regex_compile           | 174 ms                                                 | 128 ms: 1.36x faster                                                |
| async_tree_none         | 713 ms                                                 | 528 ms: 1.35x faster                                                |
| scimark_fft             | 414 ms                                                 | 308 ms: 1.34x faster                                                |
| aiohttp                 | 1.34 ms                                                | 995 us: 1.34x faster                                                |
| async_tree_io           | 1.78 sec                                               | 1.32 sec: 1.34x faster                                              |
| gunicorn                | 1.43 ms                                                | 1.07 ms: 1.34x faster                                               |
| pycparser               | 1.51 sec                                               | 1.13 sec: 1.33x faster                                              |
| deepcopy                | 429 us                                                 | 324 us: 1.33x faster                                                |
| genshi_xml              | 63.6 ms                                                | 47.9 ms: 1.33x faster                                               |
| 2to3                    | 332 ms                                                 | 252 ms: 1.32x faster                                                |
| nqueens                 | 99.3 ms                                                | 75.8 ms: 1.31x faster                                               |
| async_tree_memoization  | 854 ms                                                 | 652 ms: 1.31x faster                                                |
| deepcopy_reduce         | 3.75 us                                                | 2.88 us: 1.30x faster                                               |
| sqlglot_normalize       | 135 ms                                                 | 105 ms: 1.29x faster                                                |
| sqlglot_optimize        | 65.3 ms                                                | 51.0 ms: 1.28x faster                                               |
| docutils                | 3.18 sec                                               | 2.50 sec: 1.27x faster                                              |
| fannkuch                | 477 ms                                                 | 375 ms: 1.27x faster                                                |
| unpack_sequence         | 59.5 ns                                                | 46.9 ns: 1.27x faster                                               |
| mypy                    | 1.01 sec                                               | 802 ms: 1.26x faster                                                |
| async_tree_cpu_io_mixed | 949 ms                                                 | 760 ms: 1.25x faster                                                |
| async_generators        | 428 ms                                                 | 346 ms: 1.24x faster                                                |
| coroutines              | 31.7 ms                                                | 26.0 ms: 1.22x faster                                               |
| sympy_integrate         | 23.9 ms                                                | 19.7 ms: 1.21x faster                                               |
| dulwich_log             | 75.5 ms                                                | 62.3 ms: 1.21x faster                                               |
| json_loads              | 28.9 us                                                | 23.8 us: 1.21x faster                                               |
| bench_thread_pool       | 943 us                                                 | 784 us: 1.20x faster                                                |
| xml_etree_generate      | 93.3 ms                                                | 77.6 ms: 1.20x faster                                               |
| sympy_str               | 324 ms                                                 | 270 ms: 1.20x faster                                                |
| sympy_sum               | 183 ms                                                 | 155 ms: 1.18x faster                                                |
| sympy_expand            | 537 ms                                                 | 457 ms: 1.18x faster                                                |
| json                    | 5.35 ms                                                | 4.64 ms: 1.15x faster                                               |
| mdp                     | 2.82 sec                                               | 2.45 sec: 1.15x faster                                              |
| sqlite_synth            | 2.90 us                                                | 2.53 us: 1.15x faster                                               |
| pickle_list             | 4.50 us                                                | 3.92 us: 1.15x faster                                               |
| pathlib                 | 20.0 ms                                                | 17.8 ms: 1.12x faster                                               |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                |
| regex_v8                | 25.0 ms                                                | 22.6 ms: 1.10x faster                                               |
| unpickle                | 14.3 us                                                | 13.1 us: 1.09x faster                                               |
| meteor_contest          | 114 ms                                                 | 105 ms: 1.09x faster                                                |
| xml_etree_iterparse     | 110 ms                                                 | 102 ms: 1.08x faster                                                |
| telco                   | 6.68 ms                                                | 6.46 ms: 1.03x faster                                               |
| regex_dna               | 214 ms                                                 | 208 ms: 1.03x faster                                                |
| generators              | 75.8 ms                                                | 74.5 ms: 1.02x faster                                               |
| pickle                  | 10.1 us                                                | 10.0 us: 1.01x faster                                               |
| pidigits                | 190 ms                                                 | 191 ms: 1.00x slower                                                |
| unpickle_list           | 4.99 us                                                | 5.02 us: 1.01x slower                                               |
| pickle_dict             | 28.3 us                                                | 29.8 us: 1.05x slower                                               |
| regex_effbot            | 3.21 ms                                                | 3.44 ms: 1.07x slower                                               |
| python_startup_no_site  | 5.76 ms                                                | 6.48 ms: 1.12x slower                                               |
| coverage                | 75.3 ms                                                | 99.9 ms: 1.33x slower                                               |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                        |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (4) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20230203-3.12.0a4+-6b312e0/bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-6b312e0.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
