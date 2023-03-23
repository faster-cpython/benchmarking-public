
# Results vs. 3.11.0

- fork: python
- ref: v3.10.10
- machine: linux-x86_64
- commit hash: aad5f6a
- commit date: 2023-02-07
- overall geometric mean: 1.24x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-python-v3.10.10-3.10.10-aad5f6a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 335 ms: 1.29x slower                                     |
| chameleon      | 6.38 ms                                                | 9.13 ms: 1.43x slower                                    |
| docutils       | 2.60 sec                                               | 3.22 sec: 1.24x slower                                   |
| html5lib       | 64.8 ms                                                | 87.5 ms: 1.35x slower                                    |
| tornado_http   | 96.5 ms                                                | 130 ms: 1.35x slower                                     |
| Geometric mean | (ref)                                                  | 1.33x slower                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-python-v3.10.10-3.10.10-aad5f6a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------:|
| pidigits       | 197 ms                                                 | 189 ms: 1.04x faster                                     |
| float          | 76.8 ms                                                | 109 ms: 1.42x slower                                     |
| nbody          | 90.0 ms                                                | 137 ms: 1.52x slower                                     |
| Geometric mean | (ref)                                                  | 1.27x slower                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-python-v3.10.10-3.10.10-aad5f6a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------:|
| regex_effbot   | 3.46 ms                                                | 3.62 ms: 1.05x slower                                    |
| regex_dna      | 203 ms                                                 | 216 ms: 1.06x slower                                     |
| regex_v8       | 22.2 ms                                                | 24.1 ms: 1.09x slower                                    |
| regex_compile  | 136 ms                                                 | 177 ms: 1.29x slower                                     |
| Geometric mean | (ref)                                                  | 1.12x slower                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-python-v3.10.10-3.10.10-aad5f6a |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------:|
| pickle_dict          | 31.2 us                                                | 30.5 us: 1.02x faster                                    |
| unpickle_list        | 4.99 us                                                | 4.94 us: 1.01x faster                                    |
| pickle_list          | 4.14 us                                                | 4.17 us: 1.01x slower                                    |
| pickle               | 9.90 us                                                | 10.2 us: 1.03x slower                                    |
| xml_etree_iterparse  | 104 ms                                                 | 110 ms: 1.06x slower                                     |
| json_dumps           | 12.4 ms                                                | 13.6 ms: 1.10x slower                                    |
| unpickle             | 13.3 us                                                | 14.8 us: 1.12x slower                                    |
| json_loads           | 26.1 us                                                | 29.2 us: 1.12x slower                                    |
| xml_etree_generate   | 75.9 ms                                                | 93.0 ms: 1.23x slower                                    |
| unpickle_pure_python | 227 us                                                 | 297 us: 1.31x slower                                     |
| xml_etree_process    | 53.7 ms                                                | 74.4 ms: 1.39x slower                                    |
| pickle_pure_python   | 308 us                                                 | 449 us: 1.46x slower                                     |
| Geometric mean       | (ref)                                                  | 1.13x slower                                             |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-python-v3.10.10-3.10.10-aad5f6a |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------:|
| python_startup_no_site | 6.04 ms                                                | 5.79 ms: 1.04x faster                                    |
| python_startup         | 8.58 ms                                                | 9.33 ms: 1.09x slower                                    |
| Geometric mean         | (ref)                                                  | 1.02x slower                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-python-v3.10.10-3.10.10-aad5f6a |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 62.6 ms: 1.22x slower                                    |
| genshi_text     | 21.5 ms                                                | 30.1 ms: 1.40x slower                                    |
| django_template | 32.3 ms                                                | 46.6 ms: 1.44x slower                                    |
| mako            | 9.83 ms                                                | 14.6 ms: 1.49x slower                                    |
| Geometric mean  | (ref)                                                  | 1.38x slower                                             |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-python-v3.10.10-3.10.10-aad5f6a |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------:|
| coverage                | 99.3 ms                                                | 71.5 ms: 1.39x faster                                    |
| gc_traversal            | 3.82 ms                                                | 3.54 ms: 1.08x faster                                    |
| pidigits                | 197 ms                                                 | 189 ms: 1.04x faster                                     |
| python_startup_no_site  | 6.04 ms                                                | 5.79 ms: 1.04x faster                                    |
| pickle_dict             | 31.2 us                                                | 30.5 us: 1.02x faster                                    |
| unpickle_list           | 4.99 us                                                | 4.94 us: 1.01x faster                                    |
| pickle_list             | 4.14 us                                                | 4.17 us: 1.01x slower                                    |
| pickle                  | 9.90 us                                                | 10.2 us: 1.03x slower                                    |
| asyncio_tcp             | 883 ms                                                 | 915 ms: 1.04x slower                                     |
| generators              | 73.5 ms                                                | 76.1 ms: 1.04x slower                                    |
| telco                   | 6.43 ms                                                | 6.71 ms: 1.04x slower                                    |
| regex_effbot            | 3.46 ms                                                | 3.62 ms: 1.05x slower                                    |
| xml_etree_iterparse     | 104 ms                                                 | 110 ms: 1.06x slower                                     |
| regex_dna               | 203 ms                                                 | 216 ms: 1.06x slower                                     |
| mdp                     | 2.63 sec                                               | 2.82 sec: 1.07x slower                                   |
| create_gc_cycles        | 1.52 ms                                                | 1.63 ms: 1.08x slower                                    |
| meteor_contest          | 104 ms                                                 | 113 ms: 1.08x slower                                     |
| regex_v8                | 22.2 ms                                                | 24.1 ms: 1.09x slower                                    |
| python_startup          | 8.58 ms                                                | 9.33 ms: 1.09x slower                                    |
| pathlib                 | 18.1 ms                                                | 19.7 ms: 1.09x slower                                    |
| json_dumps              | 12.4 ms                                                | 13.6 ms: 1.10x slower                                    |
| json                    | 4.87 ms                                                | 5.40 ms: 1.11x slower                                    |
| unpickle                | 13.3 us                                                | 14.8 us: 1.12x slower                                    |
| json_loads              | 26.1 us                                                | 29.2 us: 1.12x slower                                    |
| bench_thread_pool       | 817 us                                                 | 919 us: 1.13x slower                                     |
| djangocms               | 32.5 us                                                | 36.7 us: 1.13x slower                                    |
| sympy_str               | 291 ms                                                 | 329 ms: 1.13x slower                                     |
| pylint                  | 462 ms                                                 | 524 ms: 1.13x slower                                     |
| sympy_sum               | 166 ms                                                 | 189 ms: 1.14x slower                                     |
| sympy_expand            | 475 ms                                                 | 546 ms: 1.15x slower                                     |
| sqlalchemy_imperative   | 18.1 ms                                                | 20.9 ms: 1.16x slower                                    |
| sympy_integrate         | 21.0 ms                                                | 24.4 ms: 1.16x slower                                    |
| coroutines              | 26.2 ms                                                | 30.6 ms: 1.17x slower                                    |
| scimark_sparse_mat_mult | 4.59 ms                                                | 5.39 ms: 1.18x slower                                    |
| dulwich_log             | 64.0 ms                                                | 75.4 ms: 1.18x slower                                    |
| dask                    | 365 ms                                                 | 434 ms: 1.19x slower                                     |
| flaskblogging           | 7.11 ms                                                | 8.47 ms: 1.19x slower                                    |
| async_generators        | 356 ms                                                 | 426 ms: 1.20x slower                                     |
| nqueens                 | 83.8 ms                                                | 100 ms: 1.20x slower                                     |
| sqlite_synth            | 2.48 us                                                | 2.97 us: 1.20x slower                                    |
| sqlalchemy_declarative  | 138 ms                                                 | 167 ms: 1.21x slower                                     |
| fannkuch                | 384 ms                                                 | 467 ms: 1.21x slower                                     |
| genshi_xml              | 51.4 ms                                                | 62.6 ms: 1.22x slower                                    |
| xml_etree_generate      | 75.9 ms                                                | 93.0 ms: 1.23x slower                                    |
| aiohttp                 | 1.05 ms                                                | 1.29 ms: 1.23x slower                                    |
| docutils                | 2.60 sec                                               | 3.22 sec: 1.24x slower                                   |
| sqlglot_optimize        | 52.7 ms                                                | 65.4 ms: 1.24x slower                                    |
| gunicorn                | 1.12 ms                                                | 1.39 ms: 1.25x slower                                    |
| deepcopy                | 341 us                                                 | 428 us: 1.25x slower                                     |
| scimark_fft             | 325 ms                                                 | 408 ms: 1.25x slower                                     |
| sqlglot_normalize       | 108 ms                                                 | 136 ms: 1.26x slower                                     |
| deepcopy_reduce         | 3.02 us                                                | 3.81 us: 1.26x slower                                    |
| 2to3                    | 259 ms                                                 | 335 ms: 1.29x slower                                     |
| regex_compile           | 136 ms                                                 | 177 ms: 1.29x slower                                     |
| pycparser               | 1.19 sec                                               | 1.54 sec: 1.30x slower                                   |
| unpickle_pure_python    | 227 us                                                 | 297 us: 1.31x slower                                     |
| tornado_http            | 96.5 ms                                                | 130 ms: 1.35x slower                                     |
| html5lib                | 64.8 ms                                                | 87.5 ms: 1.35x slower                                    |
| async_tree_cpu_io_mixed | 736 ms                                                 | 997 ms: 1.36x slower                                     |
| thrift                  | 760 us                                                 | 1.04 ms: 1.36x slower                                    |
| async_tree_io           | 1.30 sec                                               | 1.78 sec: 1.37x slower                                   |
| async_tree_none         | 526 ms                                                 | 721 ms: 1.37x slower                                     |
| async_tree_memoization  | 624 ms                                                 | 856 ms: 1.37x slower                                     |
| pprint_safe_repr        | 706 ms                                                 | 975 ms: 1.38x slower                                     |
| pprint_pformat          | 1.46 sec                                               | 2.02 sec: 1.39x slower                                   |
| xml_etree_process       | 53.7 ms                                                | 74.4 ms: 1.39x slower                                    |
| deepcopy_memo           | 35.8 us                                                | 49.9 us: 1.39x slower                                    |
| logging_simple          | 6.02 us                                                | 8.41 us: 1.40x slower                                    |
| genshi_text             | 21.5 ms                                                | 30.1 ms: 1.40x slower                                    |
| float                   | 76.8 ms                                                | 109 ms: 1.42x slower                                     |
| logging_format          | 6.48 us                                                | 9.20 us: 1.42x slower                                    |
| chameleon               | 6.38 ms                                                | 9.13 ms: 1.43x slower                                    |
| unpack_sequence         | 44.5 ns                                                | 64.0 ns: 1.44x slower                                    |
| django_template         | 32.3 ms                                                | 46.6 ms: 1.44x slower                                    |
| pickle_pure_python      | 308 us                                                 | 449 us: 1.46x slower                                     |
| spectral_norm           | 98.1 ms                                                | 143 ms: 1.46x slower                                     |
| sqlglot_transpile       | 1.65 ms                                                | 2.41 ms: 1.46x slower                                    |
| scimark_lu              | 108 ms                                                 | 160 ms: 1.48x slower                                     |
| hexiom                  | 6.34 ms                                                | 9.42 ms: 1.49x slower                                    |
| mako                    | 9.83 ms                                                | 14.6 ms: 1.49x slower                                    |
| sqlglot_parse           | 1.36 ms                                                | 2.03 ms: 1.49x slower                                    |
| crypto_pyaes            | 75.7 ms                                                | 115 ms: 1.52x slower                                     |
| nbody                   | 90.0 ms                                                | 137 ms: 1.52x slower                                     |
| scimark_monte_carlo     | 68.0 ms                                                | 105 ms: 1.55x slower                                     |
| chaos                   | 68.7 ms                                                | 106 ms: 1.55x slower                                     |
| richards                | 46.1 ms                                                | 72.6 ms: 1.57x slower                                    |
| pyflate                 | 419 ms                                                 | 659 ms: 1.57x slower                                     |
| raytrace                | 291 ms                                                 | 463 ms: 1.59x slower                                     |
| go                      | 140 ms                                                 | 226 ms: 1.61x slower                                     |
| scimark_sor             | 115 ms                                                 | 193 ms: 1.68x slower                                     |
| logging_silent          | 98.0 ns                                                | 174 ns: 1.78x slower                                     |
| deltablue               | 3.66 ms                                                | 7.41 ms: 2.03x slower                                    |
| Geometric mean          | (ref)                                                  | 1.24x slower                                             |

Benchmark hidden because not significant (3): bench_mp_pool, xml_etree_parse, mypy2
