
# Results vs. 3.11.0

- fork: python
- ref: v3.10.10
- machine: linux-x86_64
- commit hash: aad5f6a
- commit date: 2023-02-07
- overall geometric mean: 1.26x slower \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-python-v3.10.10-3.10.10-aad5f6a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------:|
| 2to3           | 257 ms                                                 | 335 ms: 1.30x slower                                     |
| chameleon      | 6.41 ms                                                | 9.13 ms: 1.42x slower                                    |
| docutils       | 2.60 sec                                               | 3.22 sec: 1.24x slower                                   |
| html5lib       | 63.2 ms                                                | 87.5 ms: 1.39x slower                                    |
| tornado_http   | 96.6 ms                                                | 130 ms: 1.35x slower                                     |
| Geometric mean | (ref)                                                  | 1.34x slower                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-python-v3.10.10-3.10.10-aad5f6a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------:|
| pidigits       | 199 ms                                                 | 189 ms: 1.06x faster                                     |
| float          | 76.3 ms                                                | 109 ms: 1.43x slower                                     |
| nbody          | 95.0 ms                                                | 137 ms: 1.44x slower                                     |
| Geometric mean | (ref)                                                  | 1.25x slower                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-python-v3.10.10-3.10.10-aad5f6a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------:|
| regex_dna      | 203 ms                                                 | 216 ms: 1.06x slower                                     |
| regex_effbot   | 3.36 ms                                                | 3.62 ms: 1.08x slower                                    |
| regex_v8       | 22.3 ms                                                | 24.1 ms: 1.08x slower                                    |
| regex_compile  | 136 ms                                                 | 177 ms: 1.30x slower                                     |
| Geometric mean | (ref)                                                  | 1.13x slower                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-python-v3.10.10-3.10.10-aad5f6a |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------:|
| pickle_dict          | 31.4 us                                                | 30.5 us: 1.03x faster                                    |
| xml_etree_parse      | 158 ms                                                 | 161 ms: 1.02x slower                                     |
| pickle               | 9.79 us                                                | 10.2 us: 1.04x slower                                    |
| json_dumps           | 12.7 ms                                                | 13.6 ms: 1.07x slower                                    |
| xml_etree_iterparse  | 103 ms                                                 | 110 ms: 1.08x slower                                     |
| json_loads           | 26.2 us                                                | 29.2 us: 1.12x slower                                    |
| unpickle             | 13.3 us                                                | 14.8 us: 1.12x slower                                    |
| xml_etree_generate   | 76.2 ms                                                | 93.0 ms: 1.22x slower                                    |
| unpickle_pure_python | 225 us                                                 | 297 us: 1.32x slower                                     |
| xml_etree_process    | 53.8 ms                                                | 74.4 ms: 1.38x slower                                    |
| pickle_pure_python   | 304 us                                                 | 449 us: 1.48x slower                                     |
| Geometric mean       | (ref)                                                  | 1.13x slower                                             |

Benchmark hidden because not significant (2): unpickle_list, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-python-v3.10.10-3.10.10-aad5f6a |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------:|
| python_startup_no_site | 5.96 ms                                                | 5.79 ms: 1.03x faster                                    |
| python_startup         | 8.36 ms                                                | 9.33 ms: 1.12x slower                                    |
| Geometric mean         | (ref)                                                  | 1.04x slower                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-python-v3.10.10-3.10.10-aad5f6a |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------:|
| genshi_xml      | 52.1 ms                                                | 62.6 ms: 1.20x slower                                    |
| genshi_text     | 22.1 ms                                                | 30.1 ms: 1.36x slower                                    |
| django_template | 32.5 ms                                                | 46.6 ms: 1.44x slower                                    |
| mako            | 9.85 ms                                                | 14.6 ms: 1.48x slower                                    |
| Geometric mean  | (ref)                                                  | 1.37x slower                                             |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-python-v3.10.10-3.10.10-aad5f6a |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------:|
| coverage                | 101 ms                                                 | 71.5 ms: 1.41x faster                                    |
| pidigits                | 199 ms                                                 | 189 ms: 1.06x faster                                     |
| pickle_dict             | 31.4 us                                                | 30.5 us: 1.03x faster                                    |
| python_startup_no_site  | 5.96 ms                                                | 5.79 ms: 1.03x faster                                    |
| telco                   | 6.62 ms                                                | 6.71 ms: 1.01x slower                                    |
| xml_etree_parse         | 158 ms                                                 | 161 ms: 1.02x slower                                     |
| pickle                  | 9.79 us                                                | 10.2 us: 1.04x slower                                    |
| generators              | 72.2 ms                                                | 76.1 ms: 1.05x slower                                    |
| regex_dna               | 203 ms                                                 | 216 ms: 1.06x slower                                     |
| json_dumps              | 12.7 ms                                                | 13.6 ms: 1.07x slower                                    |
| mdp                     | 2.62 sec                                               | 2.82 sec: 1.07x slower                                   |
| xml_etree_iterparse     | 103 ms                                                 | 110 ms: 1.08x slower                                     |
| regex_effbot            | 3.36 ms                                                | 3.62 ms: 1.08x slower                                    |
| meteor_contest          | 105 ms                                                 | 113 ms: 1.08x slower                                     |
| regex_v8                | 22.3 ms                                                | 24.1 ms: 1.08x slower                                    |
| pathlib                 | 18.2 ms                                                | 19.7 ms: 1.09x slower                                    |
| json                    | 4.95 ms                                                | 5.40 ms: 1.09x slower                                    |
| json_loads              | 26.2 us                                                | 29.2 us: 1.12x slower                                    |
| python_startup          | 8.36 ms                                                | 9.33 ms: 1.12x slower                                    |
| unpickle                | 13.3 us                                                | 14.8 us: 1.12x slower                                    |
| pylint                  | 463 ms                                                 | 524 ms: 1.13x slower                                     |
| bench_thread_pool       | 810 us                                                 | 919 us: 1.14x slower                                     |
| sympy_sum               | 166 ms                                                 | 189 ms: 1.14x slower                                     |
| sympy_str               | 287 ms                                                 | 329 ms: 1.15x slower                                     |
| sympy_expand            | 472 ms                                                 | 546 ms: 1.16x slower                                     |
| sqlalchemy_imperative   | 18.0 ms                                                | 20.9 ms: 1.16x slower                                    |
| sympy_integrate         | 20.9 ms                                                | 24.4 ms: 1.17x slower                                    |
| coroutines              | 26.1 ms                                                | 30.6 ms: 1.18x slower                                    |
| nqueens                 | 85.0 ms                                                | 100 ms: 1.18x slower                                     |
| dulwich_log             | 63.9 ms                                                | 75.4 ms: 1.18x slower                                    |
| async_generators        | 359 ms                                                 | 426 ms: 1.18x slower                                     |
| sqlite_synth            | 2.49 us                                                | 2.97 us: 1.19x slower                                    |
| flaskblogging           | 7.08 ms                                                | 8.47 ms: 1.20x slower                                    |
| genshi_xml              | 52.1 ms                                                | 62.6 ms: 1.20x slower                                    |
| fannkuch                | 388 ms                                                 | 467 ms: 1.20x slower                                     |
| sqlalchemy_declarative  | 139 ms                                                 | 167 ms: 1.20x slower                                     |
| xml_etree_generate      | 76.2 ms                                                | 93.0 ms: 1.22x slower                                    |
| scimark_sparse_mat_mult | 4.40 ms                                                | 5.39 ms: 1.23x slower                                    |
| sqlglot_optimize        | 53.0 ms                                                | 65.4 ms: 1.23x slower                                    |
| aiohttp                 | 1.05 ms                                                | 1.29 ms: 1.24x slower                                    |
| scimark_fft             | 329 ms                                                 | 408 ms: 1.24x slower                                     |
| gunicorn                | 1.12 ms                                                | 1.39 ms: 1.24x slower                                    |
| docutils                | 2.60 sec                                               | 3.22 sec: 1.24x slower                                   |
| deepcopy                | 344 us                                                 | 428 us: 1.25x slower                                     |
| sqlglot_normalize       | 108 ms                                                 | 136 ms: 1.26x slower                                     |
| deepcopy_reduce         | 2.97 us                                                | 3.81 us: 1.28x slower                                    |
| regex_compile           | 136 ms                                                 | 177 ms: 1.30x slower                                     |
| 2to3                    | 257 ms                                                 | 335 ms: 1.30x slower                                     |
| pycparser               | 1.17 sec                                               | 1.54 sec: 1.31x slower                                   |
| unpickle_pure_python    | 225 us                                                 | 297 us: 1.32x slower                                     |
| async_tree_cpu_io_mixed | 752 ms                                                 | 997 ms: 1.33x slower                                     |
| tornado_http            | 96.6 ms                                                | 130 ms: 1.35x slower                                     |
| genshi_text             | 22.1 ms                                                | 30.1 ms: 1.36x slower                                    |
| async_tree_none         | 529 ms                                                 | 721 ms: 1.36x slower                                     |
| async_tree_io           | 1.31 sec                                               | 1.78 sec: 1.36x slower                                   |
| deepcopy_memo           | 36.4 us                                                | 49.9 us: 1.37x slower                                    |
| async_tree_memoization  | 625 ms                                                 | 856 ms: 1.37x slower                                     |
| thrift                  | 752 us                                                 | 1.04 ms: 1.38x slower                                    |
| xml_etree_process       | 53.8 ms                                                | 74.4 ms: 1.38x slower                                    |
| html5lib                | 63.2 ms                                                | 87.5 ms: 1.39x slower                                    |
| logging_simple          | 6.06 us                                                | 8.41 us: 1.39x slower                                    |
| logging_format          | 6.62 us                                                | 9.20 us: 1.39x slower                                    |
| pprint_pformat          | 1.44 sec                                               | 2.02 sec: 1.40x slower                                   |
| pprint_safe_repr        | 691 ms                                                 | 975 ms: 1.41x slower                                     |
| chameleon               | 6.41 ms                                                | 9.13 ms: 1.42x slower                                    |
| float                   | 76.3 ms                                                | 109 ms: 1.43x slower                                     |
| spectral_norm           | 99.9 ms                                                | 143 ms: 1.43x slower                                     |
| django_template         | 32.5 ms                                                | 46.6 ms: 1.44x slower                                    |
| nbody                   | 95.0 ms                                                | 137 ms: 1.44x slower                                     |
| sqlglot_transpile       | 1.66 ms                                                | 2.41 ms: 1.45x slower                                    |
| unpack_sequence         | 43.4 ns                                                | 64.0 ns: 1.47x slower                                    |
| pickle_pure_python      | 304 us                                                 | 449 us: 1.48x slower                                     |
| sqlglot_parse           | 1.37 ms                                                | 2.03 ms: 1.48x slower                                    |
| mako                    | 9.85 ms                                                | 14.6 ms: 1.48x slower                                    |
| hexiom                  | 6.35 ms                                                | 9.42 ms: 1.48x slower                                    |
| scimark_lu              | 107 ms                                                 | 160 ms: 1.49x slower                                     |
| scimark_monte_carlo     | 68.3 ms                                                | 105 ms: 1.54x slower                                     |
| chaos                   | 68.6 ms                                                | 106 ms: 1.55x slower                                     |
| crypto_pyaes            | 73.9 ms                                                | 115 ms: 1.56x slower                                     |
| richards                | 46.2 ms                                                | 72.6 ms: 1.57x slower                                    |
| go                      | 143 ms                                                 | 226 ms: 1.58x slower                                     |
| pyflate                 | 417 ms                                                 | 659 ms: 1.58x slower                                     |
| raytrace                | 290 ms                                                 | 463 ms: 1.59x slower                                     |
| scimark_sor             | 115 ms                                                 | 193 ms: 1.68x slower                                     |
| logging_silent          | 98.5 ns                                                | 174 ns: 1.77x slower                                     |
| deltablue               | 3.64 ms                                                | 7.41 ms: 2.03x slower                                    |
| Geometric mean          | (ref)                                                  | 1.26x slower                                             |

Benchmark hidden because not significant (3): unpickle_list, pickle_list, bench_mp_pool
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: mypy
Ignored benchmarks (6) of /home/runner/work/benchmarking/benchmarking/results/bm-20230207-3.10.10-aad5f6a/bm-20230207-linux-x86_64-python-v3.10.10-3.10.10-aad5f6a.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal, mypy2
