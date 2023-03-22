
# Results vs. 3.10.4

- fork: python
- ref: 3ddfa55df48a67a5972f
- machine: darwin-arm64
- commit hash: 3ddfa55
- commit date: 2022-03-07
- overall geometric mean: 1.19x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220307-darwin-arm64-python-3ddfa55df48a67a5972f-3.11.0a6-3ddfa55 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 185 ms: 1.08x faster                                                  |
| chameleon      | 5.79 ms                                                | 4.64 ms: 1.25x faster                                                 |
| docutils       | 1.78 sec                                               | 1.48 sec: 1.20x faster                                                |
| html5lib       | 44.2 ms                                                | 33.3 ms: 1.33x faster                                                 |
| tornado_http   | 91.5 ms                                                | 73.9 ms: 1.24x faster                                                 |
| Geometric mean | (ref)                                                  | 1.22x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220307-darwin-arm64-python-3ddfa55df48a67a5972f-3.11.0a6-3ddfa55 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 93.3 ms                                                | 66.0 ms: 1.41x faster                                                 |
| float          | 72.4 ms                                                | 53.8 ms: 1.35x faster                                                 |
| pidigits       | 282 ms                                                 | 282 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.24x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220307-darwin-arm64-python-3ddfa55df48a67a5972f-3.11.0a6-3ddfa55 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 96.4 ms                                                | 76.1 ms: 1.27x faster                                                 |
| regex_effbot   | 2.46 ms                                                | 2.45 ms: 1.00x faster                                                 |
| regex_dna      | 162 ms                                                 | 162 ms: 1.00x slower                                                  |
| regex_v8       | 17.6 ms                                                | 18.2 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220307-darwin-arm64-python-3ddfa55df48a67a5972f-3.11.0a6-3ddfa55 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 283 us                                                 | 205 us: 1.38x faster                                                  |
| xml_etree_process    | 44.8 ms                                                | 35.7 ms: 1.25x faster                                                 |
| unpickle_pure_python | 203 us                                                 | 169 us: 1.20x faster                                                  |
| xml_etree_generate   | 54.2 ms                                                | 48.0 ms: 1.13x faster                                                 |
| xml_etree_parse      | 106 ms                                                 | 95.4 ms: 1.12x faster                                                 |
| xml_etree_iterparse  | 72.3 ms                                                | 64.8 ms: 1.12x faster                                                 |
| json_dumps           | 8.40 ms                                                | 7.68 ms: 1.09x faster                                                 |
| json_loads           | 16.9 us                                                | 16.1 us: 1.05x faster                                                 |
| unpickle_list        | 2.69 us                                                | 2.63 us: 1.02x faster                                                 |
| pickle               | 7.35 us                                                | 7.24 us: 1.02x faster                                                 |
| pickle_list          | 2.80 us                                                | 2.83 us: 1.01x slower                                                 |
| pickle_dict          | 17.9 us                                                | 18.2 us: 1.01x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.10x faster                                                          |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220307-darwin-arm64-python-3ddfa55df48a67a5972f-3.11.0a6-3ddfa55 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 8.88 ms                                                | 7.12 ms: 1.25x faster                                                 |
| python_startup         | 11.9 ms                                                | 12.9 ms: 1.08x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220307-darwin-arm64-python-3ddfa55df48a67a5972f-3.11.0a6-3ddfa55 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 10.5 ms                                                | 7.66 ms: 1.37x faster                                                 |
| django_template | 27.3 ms                                                | 22.2 ms: 1.23x faster                                                 |
| genshi_text     | 18.4 ms                                                | 15.0 ms: 1.22x faster                                                 |
| genshi_xml      | 37.2 ms                                                | 31.6 ms: 1.18x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.25x faster                                                          |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220307-darwin-arm64-python-3ddfa55df48a67a5972f-3.11.0a6-3ddfa55 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deltablue               | 5.14 ms                                                | 2.97 ms: 1.73x faster                                                 |
| logging_silent          | 119 ns                                                 | 73.9 ns: 1.62x faster                                                 |
| scimark_sor             | 126 ms                                                 | 80.0 ms: 1.58x faster                                                 |
| richards                | 51.4 ms                                                | 33.4 ms: 1.54x faster                                                 |
| logging_simple          | 4.63 us                                                | 3.03 us: 1.53x faster                                                 |
| go                      | 165 ms                                                 | 109 ms: 1.52x faster                                                  |
| raytrace                | 325 ms                                                 | 216 ms: 1.50x faster                                                  |
| logging_format          | 4.97 us                                                | 3.31 us: 1.50x faster                                                 |
| scimark_lu              | 109 ms                                                 | 74.7 ms: 1.46x faster                                                 |
| async_tree_io           | 1.02 sec                                               | 701 ms: 1.45x faster                                                  |
| nbody                   | 93.3 ms                                                | 66.0 ms: 1.41x faster                                                 |
| scimark_monte_carlo     | 72.5 ms                                                | 51.3 ms: 1.41x faster                                                 |
| async_tree_none         | 400 ms                                                 | 284 ms: 1.41x faster                                                  |
| pyflate                 | 453 ms                                                 | 325 ms: 1.40x faster                                                  |
| chaos                   | 66.7 ms                                                | 48.2 ms: 1.39x faster                                                 |
| pathlib                 | 28.8 ms                                                | 20.8 ms: 1.38x faster                                                 |
| pickle_pure_python      | 283 us                                                 | 205 us: 1.38x faster                                                  |
| mako                    | 10.5 ms                                                | 7.66 ms: 1.37x faster                                                 |
| crypto_pyaes            | 78.1 ms                                                | 57.2 ms: 1.37x faster                                                 |
| hexiom                  | 6.32 ms                                                | 4.66 ms: 1.36x faster                                                 |
| float                   | 72.4 ms                                                | 53.8 ms: 1.35x faster                                                 |
| html5lib                | 44.2 ms                                                | 33.3 ms: 1.33x faster                                                 |
| async_tree_memoization  | 490 ms                                                 | 376 ms: 1.30x faster                                                  |
| thrift                  | 580 us                                                 | 446 us: 1.30x faster                                                  |
| regex_compile           | 96.4 ms                                                | 76.1 ms: 1.27x faster                                                 |
| deepcopy_memo           | 34.4 us                                                | 27.4 us: 1.26x faster                                                 |
| xml_etree_process       | 44.8 ms                                                | 35.7 ms: 1.25x faster                                                 |
| aiohttp                 | 1.27 ms                                                | 1.01 ms: 1.25x faster                                                 |
| spectral_norm           | 95.8 ms                                                | 76.6 ms: 1.25x faster                                                 |
| chameleon               | 5.79 ms                                                | 4.64 ms: 1.25x faster                                                 |
| python_startup_no_site  | 8.88 ms                                                | 7.12 ms: 1.25x faster                                                 |
| async_tree_cpu_io_mixed | 669 ms                                                 | 538 ms: 1.24x faster                                                  |
| pycparser               | 916 ms                                                 | 739 ms: 1.24x faster                                                  |
| tornado_http            | 91.5 ms                                                | 73.9 ms: 1.24x faster                                                 |
| dulwich_log             | 37.1 ms                                                | 30.0 ms: 1.24x faster                                                 |
| pprint_safe_repr        | 606 ms                                                 | 490 ms: 1.24x faster                                                  |
| pprint_pformat          | 1.23 sec                                               | 998 ms: 1.23x faster                                                  |
| django_template         | 27.3 ms                                                | 22.2 ms: 1.23x faster                                                 |
| genshi_text             | 18.4 ms                                                | 15.0 ms: 1.22x faster                                                 |
| deepcopy                | 281 us                                                 | 232 us: 1.21x faster                                                  |
| gunicorn                | 1.35 ms                                                | 1.12 ms: 1.21x faster                                                 |
| unpickle_pure_python    | 203 us                                                 | 169 us: 1.20x faster                                                  |
| docutils                | 1.78 sec                                               | 1.48 sec: 1.20x faster                                                |
| async_generators        | 234 ms                                                 | 195 ms: 1.20x faster                                                  |
| fannkuch                | 317 ms                                                 | 266 ms: 1.19x faster                                                  |
| flaskblogging           | 2.75 ms                                                | 2.31 ms: 1.19x faster                                                 |
| sqlalchemy_imperative   | 8.89 ms                                                | 7.49 ms: 1.19x faster                                                 |
| deepcopy_reduce         | 2.37 us                                                | 2.01 us: 1.18x faster                                                 |
| genshi_xml              | 37.2 ms                                                | 31.6 ms: 1.18x faster                                                 |
| sqlglot_transpile       | 1.57 ms                                                | 1.35 ms: 1.16x faster                                                 |
| sqlalchemy_declarative  | 74.9 ms                                                | 64.4 ms: 1.16x faster                                                 |
| sqlglot_parse           | 1.37 ms                                                | 1.18 ms: 1.16x faster                                                 |
| sqlglot_optimize        | 38.0 ms                                                | 32.9 ms: 1.16x faster                                                 |
| sympy_integrate         | 13.3 ms                                                | 11.5 ms: 1.15x faster                                                 |
| scimark_fft             | 230 ms                                                 | 203 ms: 1.14x faster                                                  |
| sqlite_synth            | 1.47 us                                                | 1.30 us: 1.13x faster                                                 |
| xml_etree_generate      | 54.2 ms                                                | 48.0 ms: 1.13x faster                                                 |
| generators              | 32.7 ms                                                | 29.0 ms: 1.13x faster                                                 |
| sqlglot_normalize       | 196 ms                                                 | 175 ms: 1.12x faster                                                  |
| xml_etree_parse         | 106 ms                                                 | 95.4 ms: 1.12x faster                                                 |
| xml_etree_iterparse     | 72.3 ms                                                | 64.8 ms: 1.12x faster                                                 |
| pylint                  | 307 ms                                                 | 276 ms: 1.11x faster                                                  |
| nqueens                 | 68.2 ms                                                | 61.2 ms: 1.11x faster                                                 |
| sympy_str               | 169 ms                                                 | 152 ms: 1.11x faster                                                  |
| bench_thread_pool       | 546 us                                                 | 495 us: 1.10x faster                                                  |
| sympy_sum               | 93.6 ms                                                | 84.9 ms: 1.10x faster                                                 |
| sympy_expand            | 275 ms                                                 | 250 ms: 1.10x faster                                                  |
| json_dumps              | 8.40 ms                                                | 7.68 ms: 1.09x faster                                                 |
| json                    | 3.08 ms                                                | 2.83 ms: 1.09x faster                                                 |
| 2to3                    | 201 ms                                                 | 185 ms: 1.08x faster                                                  |
| coroutines              | 20.2 ms                                                | 18.7 ms: 1.08x faster                                                 |
| scimark_sparse_mat_mult | 3.46 ms                                                | 3.25 ms: 1.06x faster                                                 |
| mdp                     | 1.66 sec                                               | 1.58 sec: 1.05x faster                                                |
| meteor_contest          | 78.1 ms                                                | 74.3 ms: 1.05x faster                                                 |
| json_loads              | 16.9 us                                                | 16.1 us: 1.05x faster                                                 |
| telco                   | 3.63 ms                                                | 3.51 ms: 1.04x faster                                                 |
| unpickle_list           | 2.69 us                                                | 2.63 us: 1.02x faster                                                 |
| pickle                  | 7.35 us                                                | 7.24 us: 1.02x faster                                                 |
| regex_effbot            | 2.46 ms                                                | 2.45 ms: 1.00x faster                                                 |
| pidigits                | 282 ms                                                 | 282 ms: 1.00x faster                                                  |
| regex_dna               | 162 ms                                                 | 162 ms: 1.00x slower                                                  |
| pickle_list             | 2.80 us                                                | 2.83 us: 1.01x slower                                                 |
| pickle_dict             | 17.9 us                                                | 18.2 us: 1.01x slower                                                 |
| regex_v8                | 17.6 ms                                                | 18.2 ms: 1.03x slower                                                 |
| python_startup          | 11.9 ms                                                | 12.9 ms: 1.08x slower                                                 |
| bench_mp_pool           | 39.7 ms                                                | 44.8 ms: 1.13x slower                                                 |
| coverage                | 42.0 ms                                                | 50.4 ms: 1.20x slower                                                 |
| unpack_sequence         | 37.4 ns                                                | 90.4 ns: 2.42x slower                                                 |
| Geometric mean          | (ref)                                                  | 1.19x faster                                                          |

Benchmark hidden because not significant (1): unpickle
Ignored benchmarks (6) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp, comprehensions, create_gc_cycles, dask, gc_traversal, mypy2
