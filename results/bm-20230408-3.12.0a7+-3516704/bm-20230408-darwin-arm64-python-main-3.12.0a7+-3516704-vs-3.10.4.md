
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: 3516704
- commit date: 2023-04-08
- overall geometric mean: 1.20x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230408-darwin-arm64-python-main-3.12.0a7+-3516704 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 168 ms: 1.20x faster                                   |
| chameleon      | 5.79 ms                                                | 4.50 ms: 1.29x faster                                  |
| docutils       | 1.78 sec                                               | 1.50 sec: 1.19x faster                                 |
| html5lib       | 44.2 ms                                                | 36.6 ms: 1.21x faster                                  |
| tornado_http   | 91.5 ms                                                | 71.0 ms: 1.29x faster                                  |
| Geometric mean | (ref)                                                  | 1.23x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230408-darwin-arm64-python-main-3.12.0a7+-3516704 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 93.3 ms                                                | 60.4 ms: 1.55x faster                                  |
| float          | 72.4 ms                                                | 52.9 ms: 1.37x faster                                  |
| pidigits       | 282 ms                                                 | 280 ms: 1.01x faster                                   |
| Geometric mean | (ref)                                                  | 1.29x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230408-darwin-arm64-python-main-3.12.0a7+-3516704 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 96.4 ms                                                | 76.7 ms: 1.26x faster                                  |
| regex_v8       | 17.6 ms                                                | 16.1 ms: 1.09x faster                                  |
| regex_dna      | 162 ms                                                 | 152 ms: 1.06x faster                                   |
| regex_effbot   | 2.46 ms                                                | 2.67 ms: 1.08x slower                                  |
| Geometric mean | (ref)                                                  | 1.08x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230408-darwin-arm64-python-main-3.12.0a7+-3516704 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 283 us                                                 | 194 us: 1.46x faster                                   |
| unpickle_pure_python | 203 us                                                 | 149 us: 1.37x faster                                   |
| json_dumps           | 8.40 ms                                                | 6.27 ms: 1.34x faster                                  |
| xml_etree_process    | 44.8 ms                                                | 36.8 ms: 1.22x faster                                  |
| xml_etree_parse      | 106 ms                                                 | 98.0 ms: 1.09x faster                                  |
| unpickle             | 9.89 us                                                | 9.11 us: 1.08x faster                                  |
| xml_etree_generate   | 54.2 ms                                                | 51.5 ms: 1.05x faster                                  |
| json_loads           | 16.9 us                                                | 16.4 us: 1.03x faster                                  |
| xml_etree_iterparse  | 72.3 ms                                                | 71.2 ms: 1.02x faster                                  |
| unpickle_list        | 2.69 us                                                | 2.66 us: 1.01x faster                                  |
| pickle_list          | 2.80 us                                                | 2.87 us: 1.02x slower                                  |
| pickle               | 7.35 us                                                | 7.52 us: 1.02x slower                                  |
| pickle_dict          | 17.9 us                                                | 18.4 us: 1.03x slower                                  |
| Geometric mean       | (ref)                                                  | 1.11x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230408-darwin-arm64-python-main-3.12.0a7+-3516704 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 11.9 ms                                                | 11.2 ms: 1.07x faster                                  |
| python_startup_no_site | 8.88 ms                                                | 9.23 ms: 1.04x slower                                  |
| Geometric mean         | (ref)                                                  | 1.01x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230408-darwin-arm64-python-main-3.12.0a7+-3516704 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 10.5 ms                                                | 7.39 ms: 1.42x faster                                  |
| genshi_xml      | 37.2 ms                                                | 29.5 ms: 1.26x faster                                  |
| django_template | 27.3 ms                                                | 21.7 ms: 1.25x faster                                  |
| genshi_text     | 18.4 ms                                                | 14.7 ms: 1.25x faster                                  |
| Geometric mean  | (ref)                                                  | 1.29x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230408-darwin-arm64-python-main-3.12.0a7+-3516704 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 5.14 ms                                                | 2.60 ms: 1.98x faster                                  |
| logging_silent          | 119 ns                                                 | 67.3 ns: 1.77x faster                                  |
| richards                | 51.4 ms                                                | 31.4 ms: 1.64x faster                                  |
| nbody                   | 93.3 ms                                                | 60.4 ms: 1.55x faster                                  |
| scimark_lu              | 109 ms                                                 | 71.5 ms: 1.53x faster                                  |
| sqlglot_parse           | 1.37 ms                                                | 906 us: 1.51x faster                                   |
| asyncio_tcp             | 670 ms                                                 | 451 ms: 1.49x faster                                   |
| raytrace                | 325 ms                                                 | 221 ms: 1.47x faster                                   |
| async_tree_memoization  | 490 ms                                                 | 335 ms: 1.46x faster                                   |
| sqlglot_transpile       | 1.57 ms                                                | 1.08 ms: 1.46x faster                                  |
| pickle_pure_python      | 283 us                                                 | 194 us: 1.46x faster                                   |
| scimark_sor             | 126 ms                                                 | 88.2 ms: 1.43x faster                                  |
| go                      | 165 ms                                                 | 116 ms: 1.43x faster                                   |
| crypto_pyaes            | 78.1 ms                                                | 54.7 ms: 1.43x faster                                  |
| mako                    | 10.5 ms                                                | 7.39 ms: 1.42x faster                                  |
| hexiom                  | 6.32 ms                                                | 4.46 ms: 1.42x faster                                  |
| chaos                   | 66.7 ms                                                | 47.3 ms: 1.41x faster                                  |
| async_tree_none         | 400 ms                                                 | 286 ms: 1.40x faster                                   |
| async_tree_io           | 1.02 sec                                               | 735 ms: 1.39x faster                                   |
| scimark_monte_carlo     | 72.5 ms                                                | 52.5 ms: 1.38x faster                                  |
| float                   | 72.4 ms                                                | 52.9 ms: 1.37x faster                                  |
| unpickle_pure_python    | 203 us                                                 | 149 us: 1.37x faster                                   |
| pycparser               | 916 ms                                                 | 682 ms: 1.34x faster                                   |
| json_dumps              | 8.40 ms                                                | 6.27 ms: 1.34x faster                                  |
| deepcopy_memo           | 34.4 us                                                | 25.9 us: 1.33x faster                                  |
| pyflate                 | 453 ms                                                 | 342 ms: 1.32x faster                                   |
| spectral_norm           | 95.8 ms                                                | 73.1 ms: 1.31x faster                                  |
| tornado_http            | 91.5 ms                                                | 71.0 ms: 1.29x faster                                  |
| chameleon               | 5.79 ms                                                | 4.50 ms: 1.29x faster                                  |
| pprint_safe_repr        | 606 ms                                                 | 475 ms: 1.28x faster                                   |
| pprint_pformat          | 1.23 sec                                               | 968 ms: 1.27x faster                                   |
| thrift                  | 580 us                                                 | 458 us: 1.27x faster                                   |
| create_gc_cycles        | 880 us                                                 | 696 us: 1.26x faster                                   |
| genshi_xml              | 37.2 ms                                                | 29.5 ms: 1.26x faster                                  |
| deepcopy                | 281 us                                                 | 223 us: 1.26x faster                                   |
| regex_compile           | 96.4 ms                                                | 76.7 ms: 1.26x faster                                  |
| django_template         | 27.3 ms                                                | 21.7 ms: 1.25x faster                                  |
| logging_simple          | 4.63 us                                                | 3.71 us: 1.25x faster                                  |
| genshi_text             | 18.4 ms                                                | 14.7 ms: 1.25x faster                                  |
| dulwich_log             | 37.1 ms                                                | 30.1 ms: 1.23x faster                                  |
| logging_format          | 4.97 us                                                | 4.05 us: 1.23x faster                                  |
| async_tree_cpu_io_mixed | 669 ms                                                 | 545 ms: 1.23x faster                                   |
| scimark_sparse_mat_mult | 3.46 ms                                                | 2.82 ms: 1.22x faster                                  |
| scimark_fft             | 230 ms                                                 | 189 ms: 1.22x faster                                   |
| xml_etree_process       | 44.8 ms                                                | 36.8 ms: 1.22x faster                                  |
| deepcopy_reduce         | 2.37 us                                                | 1.95 us: 1.22x faster                                  |
| html5lib                | 44.2 ms                                                | 36.6 ms: 1.21x faster                                  |
| 2to3                    | 201 ms                                                 | 168 ms: 1.20x faster                                   |
| sqlalchemy_imperative   | 8.89 ms                                                | 7.47 ms: 1.19x faster                                  |
| docutils                | 1.78 sec                                               | 1.50 sec: 1.19x faster                                 |
| sqlglot_optimize        | 38.0 ms                                                | 32.0 ms: 1.19x faster                                  |
| fannkuch                | 317 ms                                                 | 269 ms: 1.18x faster                                   |
| sqlalchemy_declarative  | 74.9 ms                                                | 64.6 ms: 1.16x faster                                  |
| generators              | 32.7 ms                                                | 28.2 ms: 1.16x faster                                  |
| bench_thread_pool       | 546 us                                                 | 472 us: 1.16x faster                                   |
| mypy2                   | 307 ms                                                 | 265 ms: 1.16x faster                                   |
| unpack_sequence         | 37.4 ns                                                | 32.9 ns: 1.14x faster                                  |
| sympy_integrate         | 13.3 ms                                                | 11.8 ms: 1.13x faster                                  |
| sqlglot_normalize       | 196 ms                                                 | 176 ms: 1.12x faster                                   |
| sympy_expand            | 275 ms                                                 | 250 ms: 1.10x faster                                   |
| json                    | 3.08 ms                                                | 2.80 ms: 1.10x faster                                  |
| regex_v8                | 17.6 ms                                                | 16.1 ms: 1.09x faster                                  |
| sympy_str               | 169 ms                                                 | 156 ms: 1.09x faster                                   |
| xml_etree_parse         | 106 ms                                                 | 98.0 ms: 1.09x faster                                  |
| unpickle                | 9.89 us                                                | 9.11 us: 1.08x faster                                  |
| comprehensions          | 17.6 us                                                | 16.3 us: 1.08x faster                                  |
| mdp                     | 1.66 sec                                               | 1.54 sec: 1.08x faster                                 |
| sqlite_synth            | 1.47 us                                                | 1.37 us: 1.08x faster                                  |
| nqueens                 | 68.2 ms                                                | 63.4 ms: 1.08x faster                                  |
| coroutines              | 20.2 ms                                                | 18.8 ms: 1.07x faster                                  |
| meteor_contest          | 78.1 ms                                                | 73.2 ms: 1.07x faster                                  |
| python_startup          | 11.9 ms                                                | 11.2 ms: 1.07x faster                                  |
| regex_dna               | 162 ms                                                 | 152 ms: 1.06x faster                                   |
| sympy_sum               | 93.6 ms                                                | 88.6 ms: 1.06x faster                                  |
| telco                   | 3.63 ms                                                | 3.44 ms: 1.06x faster                                  |
| xml_etree_generate      | 54.2 ms                                                | 51.5 ms: 1.05x faster                                  |
| json_loads              | 16.9 us                                                | 16.4 us: 1.03x faster                                  |
| pathlib                 | 28.8 ms                                                | 28.1 ms: 1.02x faster                                  |
| xml_etree_iterparse     | 72.3 ms                                                | 71.2 ms: 1.02x faster                                  |
| unpickle_list           | 2.69 us                                                | 2.66 us: 1.01x faster                                  |
| pidigits                | 282 ms                                                 | 280 ms: 1.01x faster                                   |
| gc_traversal            | 2.39 ms                                                | 2.42 ms: 1.01x slower                                  |
| pickle_list             | 2.80 us                                                | 2.87 us: 1.02x slower                                  |
| pickle                  | 7.35 us                                                | 7.52 us: 1.02x slower                                  |
| pickle_dict             | 17.9 us                                                | 18.4 us: 1.03x slower                                  |
| python_startup_no_site  | 8.88 ms                                                | 9.23 ms: 1.04x slower                                  |
| regex_effbot            | 2.46 ms                                                | 2.67 ms: 1.08x slower                                  |
| async_generators        | 234 ms                                                 | 264 ms: 1.13x slower                                   |
| bench_mp_pool           | 39.7 ms                                                | 45.4 ms: 1.14x slower                                  |
| dask                    | 265 ms                                                 | 327 ms: 1.23x slower                                   |
| coverage                | 42.0 ms                                                | 60.9 ms: 1.45x slower                                  |
| Geometric mean          | (ref)                                                  | 1.20x faster                                           |
Ignored benchmarks (4) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, pylint
